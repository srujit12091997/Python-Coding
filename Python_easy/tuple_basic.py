'''You are given a tuple of numbers. Your task is to:

Print the first and last elements of the tuple.

Check if the number 10 exists in the tuple.'''

numbers = (5, 10, 15, 20, 25)

# Your code here

print("first element:", numbers[0])
print("last element:", numbers[-1])

if 10 in numbers:
    print("10 exits")
else:
    print("doesnt exist")