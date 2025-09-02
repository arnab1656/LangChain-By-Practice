from langchain_openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv() 
openai_api_key = os.getenv("OPEN_API_KEY")


llm = OpenAI(model = "gpt-3.5-turbo-instruct",openai_api_key = openai_api_key)

result  = llm.invoke("Whats the capital of India")

print(result)
