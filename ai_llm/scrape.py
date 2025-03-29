from llama_index.core.node_parser import SentenceSplitter,TokenTextSplitter
from llama_index.core import Settings,VectorStoreIndex,Document,SimpleDirectoryReader,StorageContext
from bs4 import BeautifulSoup
import requests
import llama_index
from llama_index.core import Settings,VectorStoreIndex,Document,SimpleDirectoryReader
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.llms.gemini import Gemini
import chromadb





def get_api_key(file_name):
    with open(file_name, 'r') as file:
        return file.read().strip()

#Here "Data" is the name of the directory in which the pdf is present
# Load documents from directory
#.load_data():This processes those files and returns the content of the documents so they can be used later in the program.
docs=SimpleDirectoryReader("Data").load_data()
print(docs[0])
# Define embedding and LLM models
# Embeddings are used to convert words or sentences into numbers so that the computer can understand and compare them.
gemini_embed=GeminiEmbedding(api_key=get_api_key("key.txt"),
                             model_name="models/embedding-001")
llm=Gemini(api_key=get_api_key("key.txt"),
           model_name="models/gemini-pro")






# # Set configurations
Settings.llm=llm
Settings.embed_model=gemini_embed
# dividing a larger block of text into smaller, more manageable segments or sentences.
# Each chunk of text will have 512 characters or tokens.
# When breaking the text into chunks, 20 characters from the end of one chunk will overlap with the beginning of the next chunk. This overlap helps keep context between chunks, which improves the understanding of the text.
Settings.node_parser=SentenceSplitter(chunk_size=512,chunk_overlap=20)
# Settings.node_parser=TokenTextSplitter(chunk_size=512,chunk_overlap=20)





from llama_index.vector_stores.chroma import ChromaVectorStore
load_client=chromadb.PersistentClient("./chromadb")
chroma_collection=load_client.get_or_create_collection("quickstart")
vector_store=ChromaVectorStore(chroma_collection=chroma_collection)
storage_context=StorageContext.from_defaults(vector_store=vector_store)
index=VectorStoreIndex.from_documents(docs,storage_context=storage_context,show_progress=True)






# # Create VectorStoreIndex from documents,which stores embeddings
# #  It takes the documents (docs),processes them using the embedding model, and stores the embeddings in a structure called an index. This index will help quickly find relevant parts of the documents when a question is asked.
# index=VectorStoreIndex.from_documents(docs)
#
#
#
#
#
#
#
# # Convert index to a query engine:
# # This takes the index and makes it searchable. It can now understand and respond to questions based on the information stored in the documents.
# query_engine=index.as_query_engine()
# # #Run the query
# response=query_engine.query("What is electric charge")
# print(response)