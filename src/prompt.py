from langchain_core.prompts import ChatPromptTemplate 

# This system prompt for response answer from llm model
system_prompt=(
    "you are question answer chatbot for finance "
    "you are friendly and polite"
    "answer should be of maximum three sentence and concise "
    "\n\n"
    "{context}")

prompt=ChatPromptTemplate.from_messages(
    [
        ("system",system_prompt), 
        ("human","previous chat:{chat_history}\n\n user input{input}"),
    ]
)
