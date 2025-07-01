'''def numsum(N):
    sum = 0
    for i in range(1,N+1):
        sum +=i
    return sum
print(numsum(6))'''



def numsum(N):
    sum = N*(N+1)//2
    return sum
print(numsum(20))