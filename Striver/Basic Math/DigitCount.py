#problem Statement: Given an integer N, return the number of digits in N.
'''
N=12345
count= len(str(N))
print(count)
'''
'''
N=12345
count =0
while N>0:
    N = N//10
    count += 1
print(count)'''

