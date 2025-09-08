import random


class FakeLLM:

    def __init__(self):
      print("The FakeLLM class is created")

    def predict(self,prompt):

      responseList = [
        'Delhi is the capital of India',
        'IPL is a cricket league',
        'AI stands for Artificial Intelligence'
      ] 

      return random.choice(responseList)  


class FakePromptTemplate():

    def __init__(self, template, input_variable):

      print("The FakePromptTemplate class is created")
      self.template = template
      self.input_variable = input_variable
      print("The Input varables are in constructor","  -->",template,"  -->",input_variable)

    def formato(self,input_dict ):

      print("The Input varables format ->",input_dict)
      return self.template.format(**input_dict)  #_this format is a python lib func



class FakeChain():

    def __init__(self, prompt, llm):
        print("The FakeChain constructor is called")

        self.prompt = prompt
        self.llm = llm

       

    def run(self, input_dict):

        finalPrompt = self.prompt.formato(input_dict)
        finalResult = self.llm.predict(finalPrompt)

        return finalResult



template = FakePromptTemplate(
    template = "Write a {length} Paragraph about {topic}",
    input_variable = ["length","topic"]
)

llm = FakeLLM()

# prompt = template.formato({"length":"short","topic":"football"})
# res = llm.predict("Give me the Response LLM")

chain = FakeChain(prompt = template, llm = llm)

result = chain.run({"length":"short","topic":"football"})

print("Result -> \n", result)