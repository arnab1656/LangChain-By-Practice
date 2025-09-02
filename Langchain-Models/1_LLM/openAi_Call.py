from langchain_openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv() 

# Debugg
# openai_api_key = os.getenv("OPENAI_API_KEY")
# print("Key is ->",openai_api_key)

llm = OpenAI(model = "gpt-3.5-turbo-instruct")

result  = llm.invoke("Whats the capital of India")

print(result)
