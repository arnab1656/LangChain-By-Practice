from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv() 

llm = ChatOpenAI(model="gpt-4o",temperature = 1.2)

res = llm.invoke("Hello who is the GOAT in Football")

print("Chat Model Response --->\n")
print(res.content)


