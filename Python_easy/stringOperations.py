'''You are given a string. Your task is to:

Print the first 5 characters of the string.

Check if the string contains the word "Python".

Split the string into a list of words.'''

text = "Python is a great programming language"

# Your code here

first_five = text[:5]
print(first_five)

if "Python" in text:
    print("The string contains 'Python'.")
else:
    print("doesnt match")
    
    
words = text.split()
print(words)
