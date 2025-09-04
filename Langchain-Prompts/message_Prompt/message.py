from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

message = [SystemMessage(content="You are a helpful assistant" ),HumanMessage(content ="Tell me about Messi") ]

model = ChatOpenAI()

res = model.invoke(message)

message.append(AIMessage(res.content))

print("Creafted prompmt message -> \n" ,message)