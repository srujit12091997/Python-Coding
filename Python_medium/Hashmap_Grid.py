def equilPairs(grid):
    count = 0
    row_count = defaultdict(int)
    
    for row in grid:
        row_count[tuple(row)] +=1
    for column in zip(*grid):
        count +=row_count[column]
    return count