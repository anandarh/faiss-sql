import os
import faiss
import psycopg
import time
from uuid import uuid4
from dotenv import load_dotenv
from generate_ddl import generate_all_tables_ddl
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS

# Load environment variables from .env file
load_dotenv()

# Record CPU and wall clock times before starting the database operation
start_cpu = time.process_time()
start_wall = time.time()

# Initialize VertexAI embeddings
embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")

d = len(embeddings.embed_query("hello"))

# FAISS index setup
index = faiss.IndexFlatL2(d)

vector_store = FAISS(
    embedding_function=embeddings,
    index=index,
    docstore=InMemoryDocstore(),
    index_to_docstore_id={},
)

# Establishing the database connection
try:
    connection = psycopg.connect(
        host=os.getenv('POSTGRES_HOST'),
        user=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD'),
        dbname=os.getenv('POSTGRES_DB')
    )

    # Generate DDL (Data Definition Language) for all tables in the 'public' schema
    documents = generate_all_tables_ddl(connection, 'public')

    # Generate UUIDs untuk setiap dokumen
    ddl_uuids = [str(uuid4()) for _ in range(len(documents))]

    vector_store.add_documents(
        documents=documents, ids=ddl_uuids)
    print("Dokumen dari sumber 'documentation' berhasil ditambahkan ke vector store!")

    # Record CPU and wall clock times after completing the operation
    end_cpu = time.process_time()
    end_wall = time.time()

    # Print the time taken by the process (CPU time and wall time)
    print(f"CPU times: {end_cpu - start_cpu:.4f} seconds for save vector")
    print(f"Wall time: {end_wall - start_wall:.4f} seconds for save vector")

except psycopg.Error as e:
    print(f"Error: {e}")
finally:
    connection.close()


def call_similarity(query: str):
    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={'k': 4}
    )

    return retriever.invoke(query)
