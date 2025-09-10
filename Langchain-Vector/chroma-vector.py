from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.schema import Document
from dotenv import load_dotenv

load_dotenv()

#_making the Documents...

doc1 = Document(
        page_content="Virat Kohli is one of the most successful and consistent batsmen in IPL history. Known for his aggressive batting style and fitness, he has led the Royal Challengers Bangalore in multiple seasons.",
        metadata={"team": "Royal Challengers Bangalore"}
    )
doc2 = Document(
        page_content="Rohit Sharma is the most successful captain in IPL history, leading Mumbai Indians to five titles. He's known for his calm demeanor and ability to play big innings under pressure.",
        metadata={"team": "Mumbai Indians"}
    )
doc3 = Document(
        page_content="MS Dhoni, famously known as Captain Cool, has led Chennai Super Kings to multiple IPL titles. His finishing skills, wicketkeeping, and leadership are legendary.",
        metadata={"team": "Chennai Super Kings"}
    )
doc4 = Document(
        page_content="Jasprit Bumrah is considered one of the best fast bowlers in T20 cricket. Playing for Mumbai Indians, he is known for his yorkers and death-over expertise.",
        metadata={"team": "Mumbai Indians"}
    )
doc5 = Document(
        page_content="Ravindra Jadeja is a dynamic all-rounder who contributes with both bat and ball. Representing Chennai Super Kings, his quick fielding and match-winning performances make him a key player.",
        metadata={"team": "Chennai Super Kings"}
    )


docs = [doc1,doc2,doc3,doc4,doc5]

vector_chroma_store = Chroma(embedding_function = OpenAIEmbeddings(), persist_directory = "chroma_DB_ARNAB", collection_name='sample')

#_Adding Documents
id_list = vector_chroma_store.add_documents(docs)

print("The id_list is ->",id_list)

# view documents

res = vector_chroma_store.get(include = ['embeddings','documents', 'metadatas'])

# print("The vector_chroma res is ->",res)

res1 = vector_chroma_store.similarity_search(query='Who among these are a bowler?',k=2)

print("The vector_chroma res1 is ->",res1)

res2 = vector_chroma_store.similarity_search(query='', filter={"team": "Chennai Super Kings"})

print("The vector_chroma res TWO is ->",res2)


res3 = vector_chroma_store.similarity_search_with_score(query = "Who among these are a bowler?", k=2)

print("The vector_chroma res res3 is ->",res3)

# update documents
updated_doc1 = Document(
    page_content="Virat Kohli, the former captain of Royal Challengers Bangalore (RCB), is renowned for his aggressive leadership and consistent batting performances. He holds the record for the most runs in IPL history, including multiple centuries in a single season. Despite RCB not winning an IPL title under his captaincy, Kohli's passion and fitness set a benchmark for the league. His ability to chase targets and anchor innings has made him one of the most dependable players in T20 cricket.",
    metadata={"team": "Royal Challengers Bangalore"}
)
# updating documents
vector_chroma_store.update_document(document_id = "40952bc6-e7bd-4b3c-9436-4a3752cb6791", document = updated_doc1)

#_View Documents
# view = vector_chroma_store.get(include = ['embeddings','documents', 'metadatas'])

# print("view \n",view)

# delete document
vector_chroma_store.delete(["40952bc6-e7bd-4b3c-9436-4a3752cb6791"])

#_View Documents
view = vector_chroma_store.get(include = ['embeddings','documents', 'metadatas'])

print("view \n",view)