'''def increasingTriplet(nums):
    l , r =0,1
    for i in range(len(nums)):
        if nums[l]<nums[r]:
            return True
    return False
print(increasingTriplet([6,1,2,5,3,4,5]))'''

'''def increasingTriplet(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] < nums[j]:
                for k in range(j+1, n):
                    if nums[j]< nums[k]:
                        return True
    return False
print(increasingTriplet([6,1,2,5,3,4,5]))'''

def increasingTriplet(nums):
    first = float('inf')
    second = float('inf')
    for num in nums:
        if num < first:
            first = num
        elif num <= second:
            second = num
        else:
            return True
    return False
print(increasingTriplet([1,1,1,1,1,1,1]))