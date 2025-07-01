'''def secondLargest(nums):
    nums.sort()
    largest = nums[-1]
    for i in range(1, len(nums)):
        if (nums[-i]< largest):
            return nums[i]
print(secondLargest([1,2,3,4,5,6,7,7,7]))'''


def secondlargest(nums, n):
    if (n<2):
        return -1
    small = float("inf")
    second_small= float("inf")
    for i in range(n):
        if (nums[i]< small):
            second_small = small
            small = nums[i]
        elif (nums[i]< second_small and nums[i] != small):
            second_small = nums[i]
    return second_small
print(secondlargest([1,2,3,4,5,6,7,7,7], 9))