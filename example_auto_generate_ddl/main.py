import os
import re
import psycopg
from faiss_vector import call_similarity

def get_table_structure(table_name: str) -> str:
    """Get table structure from database"""
    try:
        connection = psycopg.connect(
            host=os.getenv('POSTGRES_HOST'),
            user=os.getenv('POSTGRES_USER'),
            password=os.getenv('POSTGRES_PASSWORD'),
            dbname=os.getenv('POSTGRES_DB')
        )

        with connection.cursor() as cursor:
            # Get column information
            cursor.execute("""
                SELECT column_name, data_type, is_nullable
                FROM information_schema.columns
                WHERE table_name = %s
                ORDER BY ordinal_position;
            """, (table_name,))
            columns = cursor.fetchall()

            # Get foreign key information
            cursor.execute("""
                SELECT
                    kcu.column_name,
                    ccu.table_name AS foreign_table_name,
                    ccu.column_name AS foreign_column_name
                FROM information_schema.table_constraints AS tc
                JOIN information_schema.key_column_usage AS kcu
                    ON tc.constraint_name = kcu.constraint_name
                JOIN information_schema.constraint_column_usage AS ccu
                    ON ccu.constraint_name = tc.constraint_name
                WHERE tc.table_name = %s
                    AND tc.constraint_type = 'FOREIGN KEY';
            """, (table_name,))
            foreign_keys = cursor.fetchall()

            # Format table structure
            structure = f"Table: {table_name}\n"
            structure += "Columns:\n"
            for col in columns:
                structure += f"  - {col[0]} ({col[1]}, {'NULL' if col[2] == 'YES' else 'NOT NULL'})\n"

            if foreign_keys:
                structure += "Foreign Keys:\n"
                for fk in foreign_keys:
                    structure += f"  - {fk[0]} references {fk[1]}({fk[2]})\n"
                    # Get the referenced table structure recursively
                    referenced_structure = get_table_structure(fk[1])
                    structure += "    Referenced Table Structure:\n"
                    for line in referenced_structure.split('\n'):
                        structure += f"    {line}\n"

            return structure

    except Exception as e:
        return f"Error getting table structure: {str(e)}"
    finally:
        connection.close()

def main(user_input: str):
    print("\nStep 1: Getting schema context...")
    similar_schemas = call_similarity(user_input)

    # Extract table names from schemas
    table_names = set()
    for doc in similar_schemas:
        # Look for CREATE TABLE statements and extract table names
        matches = re.findall(r'CREATE TABLE (\w+\.)?(\w+)', doc.page_content)
        for match in matches:
            table_name = match[1]  # Get the table name without schema
            table_names.add(table_name)

    # Get complete structure for each table
    complete_schema = []
    for table_name in table_names:
        table_structure = get_table_structure(table_name)
        complete_schema.append(table_structure)

    schema_context = "\n".join(complete_schema)
    print("Schema Context:")
    print(schema_context)
    return {"schema_context": schema_context}


# Chat Loop to interact with the user
while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        break

    result = call_similarity(user_input)
    print(result)
