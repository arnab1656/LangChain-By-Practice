from langchain_community.retrievers import WikipediaRetriever

wiki_retriever = WikipediaRetriever(top_k_results = 2, lang = "en")

query = "What is the Independence Day in India"

docs = wiki_retriever.invoke(query)

print(docs[0].page_content)