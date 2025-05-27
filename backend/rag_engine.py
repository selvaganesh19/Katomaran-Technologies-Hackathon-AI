import os
from dotenv import load_dotenv
from langchain.document_loaders import TextLoader
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.text_splitter import CharacterTextSplitter

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENROUTER_API_KEY")
os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"

def load_documents():
    loader = TextLoader("backend/docs/knowledge.txt")  # Your document path
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = text_splitter.split_documents(documents)
    return docs

def build_vector_store(docs):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(docs, embeddings)
    return vectorstore

def get_rag_chain():
    docs = load_documents()
    vs = build_vector_store(docs)
    llm = ChatOpenAI(
        model_name=os.getenv("OPENROUTER_MODEL"),
        temperature=0,
        openai_api_key=os.getenv("OPENROUTER_API_KEY"),
        openai_api_base="https://openrouter.ai/api/v1",
    )
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=vs.as_retriever())
    return qa_chain
