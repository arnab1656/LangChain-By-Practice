from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("Eric-Jorgenson_The-Almanack-of-Naval-Ravikant.pdf")
docs = loader.load()

# Initialize Another Character or Text base splitter
char_splitter = CharacterTextSplitter(chunk_size = 100, chunk_overlap = 20, separator='')

char_result = char_splitter.split_documents(docs)


for r in char_result:
   print("result is -> \n", r.page_content,"\n")



# Initialize Another Recursive base splitter
recursive_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100,
)

recursive_result = recursive_splitter.split_documents(docs)


for r in recursive_result:
   print("<-- recursive_result is --> \n", r.page_content,"\n <-- end of result -->")