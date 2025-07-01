'''Poblem Statement: Given an integer N, return all divisors of N.
A divisor of an integer N is a positive integer that divides N without leaving a remainder. In other words,
if N is divisible by another integer without any remainder, then that integer is considered a divisor of N.'''

'''N = 36
for i in range(1, N+1):
    if N % i ==0:
        print(i)
        '''
'''
def get_divisors(N):
    divisors = []
    for i in range(1, N+1):
        if N%i == 0:
            divisors.append(i)
    return divisors
print(get_divisors(36))
'''
import math
def get_divisor(N):
    divisor=[]
    for i in range(1, int(math.sqrt(N+1))):
        if N % i ==0:
            divisor.append(i)
            if i != N//i:
                divisor.append(N//i)
    return sorted(divisor)
print(get_divisor(36))