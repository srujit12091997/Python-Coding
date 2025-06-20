'''You are given a list of words. Your task is to:

Join the words into a single string with spaces between them.

Print the resulting string.

Count how many times the letter "e" appears in the string.

python
'''
words = ["Python", "is", "fun", "to", "learn"]

# Your code here

single_string = " ". join(words)
print(single_string)

count_e = single_string.count("e")
print(count_e)