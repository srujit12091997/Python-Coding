'''def sortingdigits(nums):
    count0 = 0
    count1 = 0
    count2 = 0
    for num in nums:
        if num == 0:
            count0 +=1
        elif num == 1:
            count1 +=1
        else:
            count2 +=1
    return count0, count1, count2

print(sortingdigits([0,1,2,0,1,2,1,2]))'''

def sortingdigits(nums):
    n = len(nums)
    l,m,r=0,0,n-1
    while m <= r:
        if nums[m] == 0:
            nums[l] , nums[m] =nums[m], nums[l]
            l +=1
            m +=1
        elif nums[m] ==1:
            m +=1
        else:
            nums[m],nums[r] = nums[r], nums[m]
            r -=1
    return nums
print(sortingdigits([0,1,2,0,1,2,1,2]))  