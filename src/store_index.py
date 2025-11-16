from langchain.vectorstores import Chroma
from src.helper import load_pdf_files,text_splitter,download_embeddings 
from langchain.chains.combine_documents import create_stuff_documents_chain 
from langchain.chains.retrieval import create_retrieval_chain  




extracted_data=load_pdf_files("Data/")
text_chunk=text_splitter(extracted_data) 
embeddings=download_embeddings()


dir="vector_database"

vector_data=Chroma.from_documents(
    documents=text_chunk,
    persist_directory=dir, 
    embedding=embeddings
) 






