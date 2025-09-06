from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema


load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)


model = ChatHuggingFace(llm =llm)


schema = [ResponseSchema(name = "fact1", description = "Fact 1 about the personality"),ResponseSchema(name = "fact2", description = "Fact 1 about the personality"),ResponseSchema(name = "fact3", description = "Fact 1 about the personality"),ResponseSchema(name = "fact4", description = "Fact 1 about the personality")]


structureParser = StructuredOutputParser.from_response_schemas(schema)


template = PromptTemplate.from_template(
  template='Give 3 fact about the personality {topic} \n {format_instruction}',
  inpput_variables = ["topic"],
  partial_variables = {"format_instruction" : structureParser.get_format_instructions()}
)

chain = template | model | structureParser

res = chain.invoke({"topic" : "Messi"})

print("res --> \n",res)