from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate


load_dotenv()

llm = HuggingFaceEndpoint( repo_id="google/gemma-2-2b-it",task="text-generation")

model = ChatHuggingFace(llm =llm)

promptTemplate1 = PromptTemplate.from_template(
template = 'Write a  summary on the following personality. /n {topic}',
)

promptTemplate2 = PromptTemplate.from_template(
template = 'Write a 5 bullet points summary on the following text. /n {text}',
)

prompt1 = promptTemplate1.invoke({"topic":"Messi"})

res = model.invoke(prompt1)

prompt2 = promptTemplate2.invoke({"text":res.content})

res1 = model.invoke(prompt2)


print("res -> \n",res1.content)





