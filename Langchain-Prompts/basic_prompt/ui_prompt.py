from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()

llm = ChatOpenAI(model="gpt-4o",temperature = 1.2) #_Making the model
template = load_prompt("promptTemplate.json")
#Imported the Prompt


st.header("Research Paper Tool")

paper_input = st.selectbox("Select Research Paper Name",["Virat Kholi", "Lionel Messi", "Cristiano Ronaldo", "Neymar"])

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Proffesional", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )



if st.button('Summarize'):
    
    chain = template | llm
    res = chain.invoke({"paper_input" :paper_input,"style_input" : style_input,"length_input": length_input})
    st.write(res.content)


