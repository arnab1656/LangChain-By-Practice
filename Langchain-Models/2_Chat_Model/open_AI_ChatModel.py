# Paid Chat Model Services(Close Source)

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv() 

llm = ChatOpenAI(model="gpt-4o",temperature = 1.2)

messages = [
    (
        "system",
        "You are a Football Analyst. Answer the Question given to you.",
    ),
    ("human", "Hello who is the GOAT in Football"),
]

# res = llm.invoke("Hello who is the GOAT in Football")

# invoking the llm using the Array 

res = llm.invoke(messages)


print("Chat Model Response --->\n")
print(res.content)


