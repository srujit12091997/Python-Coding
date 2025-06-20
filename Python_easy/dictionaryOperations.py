'''You are given a dictionary. Your task is to:

Add a new key-value pair "country": "USA" to the dictionary.

Print all the values in the dictionary.

Check if the key "age" exists in the dictionary.

python
'''

person = {"name": "John", "age": 28, "city": "San Francisco"}

# Your code here

person["country"] = "USA"

print(person)

print(person["age"])

if "age" in person:
    print("The key 'age' exist")
else:
    print("doesn't exist")