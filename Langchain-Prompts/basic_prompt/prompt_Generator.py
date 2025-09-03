from langchain_core.prompts import PromptTemplate

paper_input_ = "Arnab Research Paper"
style_input_ = "Documented"
length_input = "Paragraph"

promptTemplate = PromptTemplate.from_template(
template = """
Please provide a detailed explanation about the sports personality or topic: "{paper_input}" with the following specifications:
Explanation Style: {style_input}  
Explanation Length: {length_input}  

1. Career Highlights:  
   - Include key achievements, records, and milestones.  
   - Mention any notable awards or recognitions.  

2. Playing Style & Techniques:  
   - Explain their unique skills, techniques, or strategies.  
   - If applicable, include simple, intuitive examples or code-like breakdowns of statistics (e.g., goals, runs, assists).

3. Analogies:  
   - Use relatable analogies to simplify complex sports terms or moments.  

If certain information is not available about this personality or topic, respond with: "Insufficient information available" instead of guessing.  
Ensure the explanation is clear, accurate, and aligned with the provided style and length.
""",
validate_template = True)

promptTemplate.save("promptTemplate.json")
