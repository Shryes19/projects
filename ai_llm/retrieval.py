import llama_index
from llama_index.core import Settings,VectorStoreIndex,Document,SimpleDirectoryReader
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.llms.gemini import Gemini
import chromadb
from llama_index.vector_stores.chroma import ChromaVectorStore

def get_api_key(file_name):
    with open(file_name, 'r') as file:
        return file.read().strip()

gemini_embed=GeminiEmbedding(api_key=get_api_key("key.txt"),
                             model_name="models/embedding-001")
llm=Gemini(api_key=get_api_key("key.txt"),
           model_name="models/gemini-pro")

# Set configurations
Settings.llm=llm
Settings.embed_model=gemini_embed

db2=chromadb.PersistentClient("./chromadb")
chroma_collection=db2.get_collection("quickstart")
vectorStore=ChromaVectorStore(chroma_collection=chroma_collection)
index=VectorStoreIndex.from_vector_store(vector_store=vectorStore)

# query_engine=index.as_query_engine()
# response=query_engine.query("what is charge")
# print(response)

chat_engine=index.as_chat_engine()
resp=chat_engine.chat("what is charge")
print(resp)

resp1=chat_engine.chat("give the unit of it")
print(resp1)
