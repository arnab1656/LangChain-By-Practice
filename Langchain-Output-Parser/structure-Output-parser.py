from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = HuggingFaceEndpoint( repo_id="google/gemma-2-2b-it",task="text-generation")

model = ChatHuggingFace(llm =llm)

promptTemplate1 = PromptTemplate.from_template(
template = 'Write a  summary on the following personality. /n {topic}',
)

promptTemplate2 = PromptTemplate.from_template(
template = 'Write a 5 bullet points summary on the following text. /n {text}',
)
 
parser = StrOutputParser()

res = model.invoke(promptTemplate1)

chain = promptTemplate1 | model | parser | promptTemplate2 | model | parser

res = chain.invoke({"topic" : "Messi"})

print("res -> \n", res)

