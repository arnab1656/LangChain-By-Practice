from langchain_huggingface.llms import HuggingFacePipeline
from langchain_huggingface import ChatHuggingFace

hf = HuggingFacePipeline.from_model_id(
    model_id="gpt2",
    task="text-generation",
    pipeline_kwargs={
        "temperature" : 1.5,
        "max_new_tokens": 10},
)

# rest is Same

model = ChatHuggingFace(llm = llm)

res = model.invoke("Who is GOAT In Football")

print(res.content)

