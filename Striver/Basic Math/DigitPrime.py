'''Problem Statement: Given an integer N, check whether it is prime or not. 
A prime number is a number that is only divisible by 1 and itself and the total number of divisors is 2.'''

def prime(N):
    count =0
    for i in range(1, N+1):
        if N % i ==0:
            count += 1
    return count ==2
print(prime(999))
