def printarr(arr, n):
    print("the reverse array is:- ")
    for i in range(len(arr)):
        print(arr[i], end="")
    print()
printarr([1,2,3,4,5], 6)

'''def revarr(arr, n):
    ans = [0] * n
    for i in range(n -1, -1,-1):
        ans[n-i-1] = arr[i]
    printarr(ans, n)
revarr([1,2,3,4,5], 5)'''
'''
def rev2pointer(arr,n):
    left, right = 0, len(arr)-1
    while left< right:
        arr[left], arr[right] = arr[right], arr[left]
        left +=1
        right -=1
    return arr
rev2pointer([5,4,3,2,1],5)'''

'''def revarr(arr,n):
    left, right = 0, len(arr)-1
    while left< right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr
revarr([1,2,3,4,5], 6)'''


