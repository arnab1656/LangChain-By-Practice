from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv

load_dotenv()


documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]


model = "sentence-transformers/all-mpnet-base-v2"

hf = HuggingFaceEndpointEmbeddings(
    model=model,
    task="feature-extraction",
)

vector = hf.embed_documents(documents)

print("Hf embedded model \n")

print(str(vector))