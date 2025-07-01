'''Problem Statement: Given an integer N return the reverse of the given number.

Note: If a number has trailing zeros, then its reverse will not include them. For e.g., reverse of 10400 will be 401 instead of 00401.'''
'''
N = 12345
Reverse_N = int(str(N)[::-1])
print(Reverse_N)
'''
"""
N = 12345

revN = 0
while N >0:
    last_digit = N % 10
    revN = revN * 10 + last_digit
    N = N//10

print(revN)
"""