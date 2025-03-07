from dotenv import load_dotenv
from langchain_google_genai import HarmCategory, HarmBlockThreshold
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
import faiss
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS
from documents_ddl import ddl_documents, ddl_uuids
from documents_sql import sql_documents, sql_uuids
import time

google_api_key = "YOUR_GOOGLE_API_KEY"


safety_settings = {
    HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
}

# Initialize VertexAI embeddings
embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004", google_api_key=google_api_key)


llm = ChatGoogleGenerativeAI(
    model="models/gemini-2.0-flash",
    temperature=0.2,
    safety_settings=safety_settings,
    api_key=google_api_key
)

d = len(embeddings.embed_query("hello"))

# FAISS index setup
index = faiss.IndexFlatL2(d)

vector_store = FAISS(
    embedding_function=embeddings,
    index=index,
    docstore=InMemoryDocstore(),
    index_to_docstore_id={},
)

vector_store.add_documents(
    documents=sql_documents, ids=sql_uuids)
print("Dokumen dari sumber 'documentation' berhasil ditambahkan ke vector store!")
print(d)


def call_similarity(user_input: str):
    # Record start times
    start_cpu = time.process_time()
    start_wall = time.time()

    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={'k': 4}
    )

    retriever_result = retriever.invoke(user_input)
    print("\n=== Documents Retriever Result ===")
    print(retriever_result)

    # Record end times
    end_cpu = time.process_time()
    end_wall = time.time()

     # Print CPU times and Wall time
    print(f"CPU times: {end_cpu - start_cpu:.4f} seconds")
    print(f"Wall time: {end_wall - start_wall:.4f} seconds")

    # Create a more detailed system prompt that asks for explanation
    messages = [
        ("system", f"""Anda adalah AI yang bertugas memvalidasi dan menjelaskan SQL query untuk menjawab pertanyaan pengguna.
        
        Tugas Anda:
        1. Periksa apakah SQL query yang ditemukan dalam dokumen RAG dapat menjawab pertanyaan pengguna
        2. Informasikan ID dan SQL query yang sesuai
        3. Jelaskan mengapa SQL query tersebut sesuai atau tidak sesuai untuk pertanyaan tersebut
        4. Jelaskan bagaimana SQL query tersebut bekerja dan data apa yang akan dihasilkan
        5. Jika ada beberapa SQL query yang relevan, jelaskan mana yang paling sesuai
        
        Dokumen RAG: {retriever_result}
        """),
        ("human", f"{user_input}"),
    ]
    
    try:
        # Invoke the LLM with the messages
        llm_verify = llm.invoke(messages)
        print("\n=== SQL Query Validation ===")
        print(llm_verify.content)
    except Exception as e:
        print(f"❌ Error during LLM validation: {e}")

    # Record end times
    end_cpu = time.process_time()
    end_wall = time.time()

    # Print CPU times and Wall time
    print(f"CPU times: {end_cpu - start_cpu:.4f} seconds")
    print(f"Wall time: {end_wall - start_wall:.4f} seconds")


# Chat Loop to interact with the user
while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        break

    call_similarity(user_input)
