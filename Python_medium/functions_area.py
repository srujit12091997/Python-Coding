'''
Write a function called calculate_area that takes the length and width of a rectangle as arguments and returns its area.
If the length or width is negative, the function should return 0.
'''

def calculate_area(length, width):
    # Your code here
    calculate_area = length * width
    
    pass

# Test cases
#print(calculate_area(5, 10))  # Output: 50
#print(calculate_area(-5, 10)) # Output: 0



multiply = lambda length, width: length*width
print(multiply(5, 10))

add = lambda length, width : length+width
print(add(15, 30))