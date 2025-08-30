def majorityElement(nums):
    element = None
    count = 0
    for num in nums:
        if count == 0:
            count = 1
            element = num
            
        elif element == num:
            count += 1
            
        else:
            count -=1
    return element