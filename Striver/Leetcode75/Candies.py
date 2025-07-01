def kidCandies(n, candies, extraCandies):
    result = []
    max_candies = max(candies)
    for c in candies:
        result.append(c+ extraCandies >= max_candies)
    return result
print(kidCandies(5, [2,3,5,1,3], 3))