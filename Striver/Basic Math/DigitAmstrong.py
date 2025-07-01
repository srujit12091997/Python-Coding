'''Problem Statement: Given an integer N, return true it is an Armstrong number otherwise return false.

An Amrstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.'''

N =153

temp = N

sum = 0

while N > 0:
    last_digit = N%10
    sum += (last_digit * last_digit  * last_digit)
    N = N//10
if sum == temp:
    print("is a amstrong number")
else:
    print("Not a amstrong number")