from llama_index.core.node_parser import SentenceSplitter,TokenTextSplitter
from llama_index.core import Settings,VectorStoreIndex,Document,SimpleDirectoryReader,StorageContext
from bs4 import BeautifulSoup
import requests
import llama_index
from llama_index.core import Settings,VectorStoreIndex,Document,SimpleDirectoryReader,load_index_from_storage
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.llms.gemini import Gemini
import chromadb
import os
def get_api_key(file_name):
    with open(file_name, 'r') as file:
        return file.read().strip()
gemini_embed=GeminiEmbedding(api_key=get_api_key("p.txt"),
                             model_name="models/embedding-001")
llm=Gemini(api_key=get_api_key("p.txt"),
           model_name="models/gemini-pro")
Settings.llm=llm
Settings.embed_model=gemini_embed

def get_index(docs,name):
    index=None
    if not os.path.exists(name):
        print("building index")
        index=VectorStoreIndex.from_documents(docs,show_progress=True)
        index.storage_context.persist(persist_dir=name)
    else:
        index=load_index_from_storage(StorageContext.from_defaults(persist_dir=name))
    return index

docs=SimpleDirectoryReader("Data").load_data()
print(docs[0])
physics_index=get_index(docs,"physics")
physics_engine=physics_index.as_query_engine()