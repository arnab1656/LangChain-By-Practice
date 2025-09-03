# Paid Chat Model Services(Close Source)

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv


load_dotenv() 

prompt =  ["Who is the GOAT in Football"]


llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

res = llm.invoke(prompt)

print(res.content)