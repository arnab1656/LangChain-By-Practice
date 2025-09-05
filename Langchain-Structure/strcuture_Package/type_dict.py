from typing import TypedDict

# This TypedDict class is use to make a structure not for the validation 

class Person(TypedDict):

   name : str
   age : int

new_person = Person({"name":"Arnab paul", "age" : 32})


print("The ans is ->", new_person)