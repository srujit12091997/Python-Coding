'''You are given a JSON string. Your task is to:

Parse the JSON string into a Python dictionary.

Print the value associated with the key "city".

Add a new key-value pair "zipcode": 12345 to the dictionary.

python
'''
import json

data_json = '{"name": "Alice", "age": 25, "city": "New York"}'

# Your code here
#print(data_json)

try:
    person_dict = json.loads(data_json)
    print(person_dict)
except:
    print("error")
    
print(person_dict["city"])

person_dict["zipcode"]= "12345"
print(person_dict)