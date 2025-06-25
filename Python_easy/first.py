# Calculate the total cost per item in this list of tuples (item, price, quantity):
# Expected: {"apple": 2.5, "banana": 3.75}


orders = [("apple", 0.5, 3), ("apple", 0.5, 2), ("banana", 0.75, 4), ("banana", 0.75, 1)]



total_cost = {}

for item, price, quantity in orders:
    cost = price * quantity
    if item in total_cost:
        total_cost[item] += cost
    else:
        total_cost[item] = cost

print(total_cost)