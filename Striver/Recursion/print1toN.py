'''def fun(i, N):
    if i > N:
        return
    print(i)
    fun(i+1, N)
fun(1,10)'''

def revfun(i, n):
    if i < n:
        return
    print(i)
    revfun(i-1, n)
revfun(10, 1)