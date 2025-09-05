from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv


load_dotenv()

model = ChatOpenAI()


chat_Histroy = [SystemMessage(content='You are a helpful AI assistant')]


while True:
   inputText =  input("You :")
   chat_Histroy.append(HumanMessage(inputText))

   if inputText.lower() == "exit":
     break

   res = model.invoke(chat_Histroy)  
   chat_Histroy.append(AIMessage(res.content))
   print("AI Bot:", res.content)

print(chat_Histroy)   