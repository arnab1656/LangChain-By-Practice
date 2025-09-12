from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv() 

documents = [
    Document(page_content="FIFA football unites the world with the biggest international tournaments like the World Cup."),
    Document(page_content="The title of GOAT (Greatest of All Time) is often debated among legendary players."),
    Document(page_content="Icons like Pelé, Maradona, Messi, and Ronaldo have shaped the sport’s history."),
    Document(page_content="Winning the FIFA Ballon d’Or is considered the highest individual honor in football."),
    Document(page_content="For fans, the GOAT is not just about stats but also the passion, magic, and moments they bring."),
]

embedding_model = OpenAIEmbeddings()

#_creating a vector store

chroma_store = Chroma.from_documents(documents = documents,embedding = embedding_model, collection_name = "Arnab_DB")

retreiver = chroma_store.as_retriever(search_kwargs = {"k": 3} )

query = "Who is Messi?"

result  = retreiver.invoke(query)

for i, d in enumerate(result): 
    print("Index ->" ,i+1)
    print(" --->")
    print(d.page_content)
    print(" <--- \n")


