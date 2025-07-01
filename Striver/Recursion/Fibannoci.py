def fib(n):
    l,r = 0,1
    for i in range(n):
        print(l, end=" ")
        l,r = r, l+r
fib(10)