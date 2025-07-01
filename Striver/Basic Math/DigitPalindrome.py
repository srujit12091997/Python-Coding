"""Problem Statement: Given an integer N, return true if it is a palindrome else return false.

A palindrome is a number that reads the same backward as forward. For example, 121, 1331, and 4554 are palindromes because they remain the same when their digits are reversed."""

'''
N = 159951

N_original = N
N_rev = 0
while N > 0:
    last_digit = N%10
    N_rev = N_rev * 10 + last_digit
    N= N//10
if N_original == N_rev:  
    print("Palindrom")
else:
    print("Not a palindrome")'''


