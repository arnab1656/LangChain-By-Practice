#_Architecture of the Runnable in Langchain...

from abc import ABC, abstractmethod
import random


class Runnable(ABC):

  @abstractmethod
  def invoke(input_data):
    pass

class FakeLLM(Runnable):

    def __init__(self):
       pass

    def invoke(self,prompt):

      responseList = [
      'Delhi is the capital of India',
      'IPL is a cricket league',
      'AI stands for Artificial Intelligence'
      ]

      print("prompt -> ", prompt)

      return {"response" : random.choice(responseList)} 


    def predict(self,prompt):

      responseList = [
        'Delhi is the capital of India',
        'IPL is a cricket league',
        'AI stands for Artificial Intelligence'
      ] 

      return random.choice(responseList)  


class FakePromptTemplate(Runnable):

    def __init__(self, template, input_variable):

      self.template = template
      self.input_variable = input_variable
      print("The Input varables are in constructor","  -->",template,"  -->",input_variable)
    
    def invoke(self, input_dict):

      print("The Input varables for invoke in template ->",input_dict)
      return self.template.format(**input_dict)  


    def formato(self,input_dict ):

      print("The Input varables format ->",input_dict)
      return self.template.format(**input_dict)  #_this format is a python lib func


class FakeStrOutputParser(Runnable):

    def __init__(self):
      pass

    def invoke(self, input_data):

      print("input_data in FakeStrOutputParser", input_data)  
      return input_data['response']  


class RunnableConnector(Runnable):

    def  __init__(self, runnable_list):
      self.runnable_list = runnable_list

    def invoke(self,input_data):

      for runnable in self.runnable_list:        
        input_data = runnable.invoke(input_data) #_here each runnable is the instance of the class given in the runnable_list List

        #_here the input_data is being having a recursive value and then again the recursive is being passed to the runnable.invoke()

      print("inputdata is  -> ",input_data)

      return input_data     

#_simple Chain

# llm = FakeLLM()

# prompt = FakePromptTemplate(template = 'Write a {length} paragraph about {topic}', input_variable = ["length","topic"]) 

# parser = FakeStrOutputParser()

# chain = RunnableConnector([ prompt, llm, parser])

# chain.invoke(input_data = {"length":"short","topic":"football"})


#Chain Connector

llm = FakeLLM()

prompt1 = FakePromptTemplate(template = 'Write a {length} paragraph about {topic}', input_variable = ["length","topic"]) 

prompt2 = FakePromptTemplate(template = 'Write {length} Question about {topic}', input_variable = ["length","topic"]) 

parser = FakeStrOutputParser()

chain1 = RunnableConnector([ prompt1, llm, parser])

chain2 = RunnableConnector([ prompt2, llm, parser])

finalChain = RunnableConnector([chain1, chain2])

finalResult = finalChain.invoke({"length": "short", "topic":"Football"})

print("finalRes --> \n ",finalChain)


