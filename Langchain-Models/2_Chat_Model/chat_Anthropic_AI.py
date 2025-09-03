from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv() 

llm = ChatAnthropic(
    model="claude-3-7-sonnet-20250219",
    temperature=1.2,
)

messages = [
    (
        "system",
        "You are a Football Analyst. Answer the Question given to you.",
    ),
    ("human", "Hello who is the GOAT in Football"),
]
res = llm.invoke(messages)


print("The Response is -> \n")
print(res.content)



