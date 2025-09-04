from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import  HumanMessage

promptTemplate = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."), #System_mes
        MessagesPlaceholder("history"), #Prev_chat
        ("human", "{question}") #Human_mes
    ]
)

chatHistory = []

with open('chat_history.txt') as f:
    chatHistory.extend(f.readlines()) 

print("chatHistory -> ", chatHistory) #debugg

res = promptTemplate.invoke({"history": chatHistory, "question": "Who is Ronaldo then?" })

print("res -> ", res) #debugg



