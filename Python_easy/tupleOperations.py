'''You are given a tuple. Your task is to:

Print the number of elements in the tuple.

Convert the tuple into a list.

Add the number 100 to the list and print it.

python
'''
numbers = (1, 2, 3, 4, 5)
# Your code here

tuple_length = len(numbers)
print(tuple_length)

numbers_list = list(numbers)
print(numbers_list)

numbers_list.append(100)
print(numbers_list)