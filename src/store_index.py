from langchain.vectorstores import Chroma
from src.helper import load_pdf_files,text_splitter,download_embeddings 
from langchain.chains.combine_documents import create_stuff_documents_chain 
from langchain.chains.retrieval import create_retrieval_chain  

# extract data from pdf files 
extracted_data=load_pdf_files("Data/")

# split text data into chunk
text_chunk=text_splitter(extracted_data) 

# download embeddings to convert text data to vector
embeddings=download_embeddings()

# directory to save vector database
dir="vector_database"

# creating vector database with huggingface embedding and save vectors locally
vector_data=Chroma.from_documents(
    documents=text_chunk,
    persist_directory=dir, 
    embedding=embeddings
) 






