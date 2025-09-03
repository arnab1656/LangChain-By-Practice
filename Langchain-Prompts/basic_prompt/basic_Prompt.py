from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv() 

llm = ChatOpenAI(model="gpt-4o",temperature = 1.2)

topic = "cat"
prompt = PromptTemplate.from_template("Tell me a joke about {topic}")
resPrompt = prompt.format(topic=topic)

print("The Prompt is -> ",resPrompt)

llmRes = llm.invoke(resPrompt)

print("The LLM response is ->\n",llmRes.content)