import json

person_json = '{"name": "Alice", "age": 25, "city": "New York"}'

# Your code here
'''
try:
    person_dict = json.loads(person_json)
    print(person_dict["name"])
except json.JSONDecodeError as e:
    print(f"error:{e}")
'''
try:
    person_dict = json.loads(person_json)
    print(person_dict["place"])
except json.JSONDecodeError as e:
    print(f"error:{e}")