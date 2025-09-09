from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("ArnabPaulResume.pdf")

docs = loader.load()

print("docs content \n -->",docs[0].page_content)

print("docs meta Data \n -->",docs[0].metadata)