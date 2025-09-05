from pydantic import BaseModel,Field
import json


#use for the both structure and the Validation of the Value

class Student(BaseModel):

  name : str = "Arnab" 
  age : int 
# email : EmailStr 
  cgpa : float = Field(gt = 0,lt = 10,default = 5,description = "This is the Student CGPA")


new_student = {"name":"Arnab paul", "age" : "27", "cgpa" :"7.74"}

student = Student(**new_student)

student_dict = dict(student) #_making a json object...

print(student_dict['age'])

student_json = student.model_dump_json()


filename = "output_JSON.json"

try:
    with open(filename,"w") as jsonFile:
        json.dump(student_json,jsonFile,indent=4)
    print("Succesfully stored the JSON Data")    

except IOError as e:
    print(f"Error writing to file: {e}")   

# print("new_student is  --->", student)
