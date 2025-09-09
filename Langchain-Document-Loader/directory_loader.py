from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader


loader = DirectoryLoader(
    path = "books",
    glob = "*.pdf",
    loader_cls = PyPDFLoader
)


try:
  docs = loader.lazy_load()

  for d in docs:
    print("Page Content is ---> \n\n\n", d.page_content)


except Exception as e:
  print("Error is ",e)  
  

