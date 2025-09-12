from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv()

documents = [
    Document(page_content="FIFA football unites the world with the biggest international tournaments like the World Cup."),
    Document(page_content="The title of GOAT (Greatest of All Time) is often debated among legendary players."),
    Document(page_content="Icons like Pelé, Maradona, Messi, and Ronaldo have shaped the sport’s history."),
    Document(page_content="Winning the FIFA Ballon d’Or is considered the highest individual honor in football."),
    Document(page_content="For fans, the GOAT is not just about stats but also the passion, magic, and moments they bring."),
]


embedding_model = OpenAIEmbeddings()


#_create a vector store...

FAISS_store = FAISS.from_documents(documents = documents , embedding = embedding_model)

retreiver = FAISS_store.as_retriever(search_type = "mmr",search_kwargs = {"k":2,"lambda_mult": 0.5, })

query = "Who is messi"

res_docs = retreiver.invoke(query)

for i,d  in enumerate(res_docs):
    print("--->")
    print(i)
    print(d.page_content)
    print("<---\n")

