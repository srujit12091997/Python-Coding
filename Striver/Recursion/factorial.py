'''def factorial(X):
    fact = 1
    for i in range(1, X+1):
        fact *= i
    return fact
print(factorial(9))'''

def factorial(X):
    if X ==1:
        return 1
    return X * factorial(X-1)
print(factorial(7))