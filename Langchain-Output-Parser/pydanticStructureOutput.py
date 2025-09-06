from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field


load_dotenv()


# Define the model
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)


class Person(BaseModel):

    name :str  = Field(description='Full Name of the person')
    age :int = Field(description='Age of the person')
    personality : list[str] = Field(description='Personality of the person')

parser =  PydanticOutputParser(pydantic_object = Person)

template = PromptTemplate(
  template = 'Generate the name, age and city of a Famous Footballer of {place} \n {format_instruction}',
  input_variables = ["place"],
  partial_variables = {"format_instruction" : parser.get_format_instructions()}
)


chain = template | model | parser

res = chain.invoke({"place" : "Argentina"})

print("res -> \n",res)
