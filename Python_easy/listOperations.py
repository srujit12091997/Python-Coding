'''You are given a list of numbers. Your task is to:

Print the sum of all numbers in the list.

Find the maximum number in the list.

Remove the last element from the list and print the updated list.'''

numbers = [10, 20, 30, 40, 50]

# Your code here

count=0
for i in numbers:
    count += i
print("sum:", count)

print("max", max(numbers))
numbers.pop()
print(numbers)