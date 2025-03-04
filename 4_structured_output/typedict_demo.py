from typing import TypedDict

class person(TypedDict):
    name:str
    age:int

new_person : person = {'name':"Sumit Kumar", 'age':30}
print(new_person)