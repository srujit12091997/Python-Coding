def binary_search(nums, target):
    left, right = 0, len(nums)-1
    
    while left <= right:
        mid = left + (right- left)//2
        
        if nums[mid]== target:
            return mid
        
        elif nums[mid]< target:
            left = mid +1
            
        else:
            right = mid -1
    return -1
        
        
        
# Example usage:
nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(binary_search(nums, target)) 