from langchain_core.prompts import ChatPromptTemplate

promptTemplate = ChatPromptTemplate.from_messages(
    [
        ('system', 'You are a helpful {domain} expert'),
        ('human', 'Explain in simple terms, what is {topic}')
    ]
)

prompt  = promptTemplate.invoke({"domain": "Football","topic" : "Offside"})

print("prompt --->",prompt)