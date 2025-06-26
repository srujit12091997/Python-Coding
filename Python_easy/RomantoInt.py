def RomanToInt(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    reverse = 0
    
    for char in reversed(s):
        curr = roman[char]
        if curr< reverse:
            total -= curr
        else:
            total += curr
    return total
print(RomanToInt(s = "XXX"))