from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template = 'Write a summary from the following poem - \n {poem}',
    input_variable = ["poem"])

parser = StrOutputParser()  

loader = TextLoader("cricket.txt",encoding='utf-8')

docs = loader.load()

print("Content -> \n", docs[0].page_content)


print("meta data -> \n",docs[0].metadata)


chain = prompt | model | parser

res = chain.invoke({"poem" : docs[0].page_content})

print("response -> \n",res)


