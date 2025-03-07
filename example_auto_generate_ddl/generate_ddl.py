import psycopg
from langchain.docstore.document import Document


def generate_create_table_ddl(conn, table_name, schema_name='public'):
    """
    Creates a 'CREATE TABLE' DDL statement for a table from a PostgreSQL database,
    using table metadata retrieved from the information_schema.

    Args:
        conn: PostgreSQL database connection.
        table_name: Name of the table for which the DDL will be generated.
        schema_name: Name of the schema where the table is located (default 'public').

    Returns:
        String containing the 'CREATE TABLE' DDL statement.
    """

    with conn.cursor() as cursor:
        # Query to retrieve column metadata from the table
        ddl_query = """
        SELECT
            column_name,
            data_type,
            is_nullable,
            column_default,
            character_maximum_length,
            numeric_precision,
            numeric_scale
        FROM
            information_schema.columns
        WHERE
            table_name = %s AND table_schema = %s
        ORDER BY
            ordinal_position;
        """

        cursor.execute(ddl_query, (table_name, schema_name))
        columns = cursor.fetchall()

        create_table_statement = f"CREATE TABLE {schema_name}.{table_name} (\n"

        for column in columns:
            column_name, data_type, is_nullable, column_default, char_max_len, num_precision, num_scale = column

            # Adjust data type for VARCHAR with character length
            if data_type == 'character varying' and char_max_len:
                data_type = f"VARCHAR({char_max_len})"

            # Adjust data type for NUMERIC with precision and scale
            elif data_type == 'numeric' and num_precision and num_scale is not None:
                data_type = f"NUMERIC({num_precision}, {num_scale})"

            create_table_statement += f"    {column_name} {data_type}"

            # Add default value if present
            if column_default:
                create_table_statement += f" DEFAULT {column_default}"

            # Add nullability (NOT NULL or NULL)
            create_table_statement += " NOT NULL" if is_nullable == 'NO' else " NULL"

            create_table_statement += ",\n"

        create_table_statement = create_table_statement.rstrip(',\n')

        # Retrieve primary key and foreign key
        primary_keys = get_primary_keys(conn, table_name, schema_name)
        foreign_keys = get_foreign_keys(conn, table_name, schema_name)

        # Add primary key definition to DDL if present
        if primary_keys:
            create_table_statement += f",\n    PRIMARY KEY ({', '.join(primary_keys)})"

        # Add foreign key definition to DDL if present
        for fk in foreign_keys:
            fk_statement = f",\n    FOREIGN KEY ({', '.join(fk['columns'])}) REFERENCES {fk['referenced_table']} ({', '.join(fk['referenced_columns'])})"
            create_table_statement += fk_statement

        create_table_statement += "\n);"

        return create_table_statement


def get_primary_keys(conn, table_name, schema_name):
    """
    Retrieves the list of primary keys from the given table.

    Args:
        conn: PostgreSQL database connection.
        table_name: Name of the table for which the primary keys will be retrieved.
        schema_name: Name of the schema where the table is located.

    Returns:
        List containing the names of the columns that are primary keys.
    """

    with conn.cursor() as cursor:
        # Query to retrieve primary key from the table
        pk_query = """
        SELECT kcu.column_name
        FROM information_schema.table_constraints tc
        JOIN information_schema.key_column_usage kcu
        ON tc.constraint_name = kcu.constraint_name
        WHERE tc.table_name = %s
        AND tc.table_schema = %s
        AND tc.constraint_type = 'PRIMARY KEY';
        """
        cursor.execute(pk_query, (table_name, schema_name))
        primary_keys = cursor.fetchall()
        return [pk[0] for pk in primary_keys]


def get_foreign_keys(conn, table_name, schema_name):
    """
    Retrieves the list of foreign keys from the given table.

    Args:
        conn: PostgreSQL database connection.
        table_name: Name of the table for which the foreign keys will be retrieved.
        schema_name: Name of the schema where the table is located.

    Returns:
        List containing dictionaries with foreign key information, 
        including the columns, referenced table, and referenced columns.
    """

    with conn.cursor() as cursor:
        # Query to retrieve foreign key from the table
        fk_query = """
        SELECT
            kcu.column_name, 
            ccu.table_name AS referenced_table, 
            ccu.column_name AS referenced_column
        FROM 
            information_schema.table_constraints AS tc 
            JOIN information_schema.key_column_usage AS kcu
            ON tc.constraint_name = kcu.constraint_name
            JOIN information_schema.constraint_column_usage AS ccu
            ON ccu.constraint_name = tc.constraint_name
        WHERE 
            tc.constraint_type = 'FOREIGN KEY' AND tc.table_name = %s AND tc.table_schema = %s;
        """
        cursor.execute(fk_query, (table_name, schema_name))
        foreign_keys = cursor.fetchall()

        fk_dict = {}
        for column, referenced_table, referenced_column in foreign_keys:
            if referenced_table not in fk_dict:
                fk_dict[referenced_table] = {
                    "columns": [], "referenced_columns": []}
            fk_dict[referenced_table]["columns"].append(column)
            fk_dict[referenced_table]["referenced_columns"].append(
                referenced_column)

        fk_list = [
            {"columns": fk_data["columns"], "referenced_table": referenced_table,
                "referenced_columns": fk_data["referenced_columns"]}
            for referenced_table, fk_data in fk_dict.items()
        ]

        return fk_list


def generate_all_tables_ddl(conn, schema_name='public'):
    """
    Generates DDL statements for all tables in a schema.

    Args:
        conn: PostgreSQL database connection.
        schema_name: Name of the schema where the tables are located (default 'public').

    Returns:
        List containing Document objects with DDL for each table.
    """

    with conn.cursor() as cursor:
        # Query to retrieve all table names from the schema
        get_tables_query = """
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = %s
        AND table_type = 'BASE TABLE';
        """

        cursor.execute(get_tables_query, (schema_name,))
        tables = cursor.fetchall()

        documents = []
        for table in tables:
            table_name = table[0]
            ddl = generate_create_table_ddl(conn, table_name, schema_name)

            # Create Document object containing DDL and table metadata
            doc = Document(page_content=ddl, metadata={
                           "table_name": table_name, "schema": schema_name, "type": "ddl"})
            documents.append(doc)

        return documents
