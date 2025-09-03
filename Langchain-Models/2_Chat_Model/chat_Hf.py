from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv

load_dotenv() 

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3.1",
    task="text-generation",
    max_new_tokens=512,
)

chat = ChatHuggingFace(llm=llm)

messages = [
    ("system", "You are a  Football Wikipedia. Answer the Questions"),
    ("human", "Who is GOAT in Football"),
]

res =  chat.invoke(messages)

print("The Response is \n")

print(res.content)
