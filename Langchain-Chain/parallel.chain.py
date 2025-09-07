from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel


load_dotenv()


model = ChatOpenAI()


prompt1 = PromptTemplate(
    template='Generate short and simple notes from the following sports \n {topic}',
    input_variables=['text']
)


prompt2 = PromptTemplate(
    template='Generate 5 short question answers from the following sports \n {topic}',
    input_variables=['text']
)


prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}',
    input_variables=['notes', 'quiz']
)

parser = StrOutputParser()


paralleChain = RunnableParallel({
    "notes" : prompt1 | model | parser,
    "quiz" : prompt2 | model | parser
})

mergeChain = prompt3 | model | parser

mainChain = paralleChain | mergeChain

res = mainChain.invoke({"topic" : "FIFA Football"})

print("res --> \n", res)

mainChain.get_graph().print_ascii()