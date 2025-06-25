def maxArea(height):
    water = 0
    for i in range(len(height)):
        for j in range(len(height)):
            area = (j-i)* min(height[i],height[j])
        water = max(area, water)
    return water
    
print(maxArea(height = [1,8,6,2,5,4,8,3,7]))