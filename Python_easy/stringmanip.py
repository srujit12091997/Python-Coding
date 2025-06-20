'''You are given a string. Your task is to:

Count how many times the letter "a" appears in the string.

Replace all spaces in the string with hyphens (-).'''

text = "Python is fun and easy to learn"

# Your code here

count_a=text.count(" ")
print(count_a)

Replace=text.replace(" ","-")
print(Replace)

count_b=Replace.count(" ")
print(count_b)