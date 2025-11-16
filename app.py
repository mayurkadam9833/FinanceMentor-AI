from src.helper import download_embeddings
from src.prompt import *
from langchain.vectorstores import Chroma
from langchain.chains.combine_documents import create_stuff_documents_chain 
from langchain.chains.retrieval import create_retrieval_chain
from langchain.schema import AIMessage,HumanMessage
from langchain.memory import ConversationBufferMemory 
from langchain_community.llms import Ollama
from flask import Flask,render_template,request 

# Create a Flask application instance.
app=Flask(__name__)

# download huggingface embeddings 
embeddings=download_embeddings() 

# vector database path 
dir="vector_database" 

# This object (doc_search) is used later for similarity search in RAG pipelines.
doc_search=Chroma(
    persist_directory=dir, 
    embedding_function=embeddings
) 

# Create a retriever that fetches top 3 similar documents
retrival=doc_search.as_retriever(search_type="similarity",search_kwargs={"k":3})

# Load the LLM from Ollama (here using the Gemma 3 model)
llm=Ollama(model="gemma3")

# Create memory object to store conversation history
memory=ConversationBufferMemory(memory_key="chat_history",return_messages=True)

# Create a question–answer chain using "stuff" method
question_answer=create_stuff_documents_chain(llm=llm,prompt=prompt)

# Build the RAG chain
rag_chain=create_retrieval_chain(retrival,question_answer)

# Home route - renders the main HTML page
@app.route("/")
def index(): 
    return render_template("index.html")


# Chat route - handles user messages and returns bot responses
@app.route("/get",methods=["GET","POST"])
def chat(): 
    # Get user input text from AJAX request
    msg=request.form["msg"]
    print("user input:",msg)

    # Convert stored chat messages into a single string
    chat_hist_str="\n".join([
        f"user{m.content}" if isinstance(m,HumanMessage) else f"bot{m.content}"

        for m in memory.chat_memory.messages
    ]
    )

    # Call the RAG pipeline: retrieves docs + LLM answer
    response=rag_chain.invoke({"input":msg,"chat_history":chat_hist_str})

    # Extract final answer from the chain output
    answer=response["answer"]
    print("Response:",answer)

    # Store the latest messages in memory (for contextual chat)
    memory.chat_memory.add_message(HumanMessage(content=msg))
    memory.chat_memory.add_ai_message(AIMessage(content=answer))

     # Return answer back to frontend
    return str(answer)

# Run the Flask application
if __name__ == "__main__": 
    app.run(host="0.0.0.0",port=8080,debug=True)


