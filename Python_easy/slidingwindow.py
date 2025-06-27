def findMaxAverage(nums, k):
    n = len(nums)
    curr_sum =0
    for i in range(k):
        curr_sum +=nums[i]
    max_avg = curr_sum /k
    for i in range(k, n):
        curr_sum += nums[i]
        curr_sum-=nums[i-k]
        
        avg = curr_sum/k
        max_avg =max(avg, max_avg)
    return max_avg
    
print(findMaxAverage(nums = [1,12,-5,-6,50,3], k = 4))