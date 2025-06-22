def decodeData(data):
    if not data:
        print("No data provided")
        return

    characters = []
    max_x = 0
    max_y = 0

    for x, char, y in data:
        characters.append((x, y, char))
        max_x = max(max_x, x)
        max_y = max(max_y, y)
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for x, y, char in characters:
        if 0 <= y < len(grid) and 0 <= x < len(grid[y]):
            grid[y][x] = char
    for row in grid:
        print(''.join(row))


if __name__ == "__main__":
    example_data = [
        (0, '█', 0),
        (0, '█', 1),
        (0, '█', 2),
        (1, '▀', 0),
        (2, '▀', 0),
        (3, '▀', 0),
        (1, '▀', 1),
        (2, '▀', 1),
        (1, ' ', 2),
        (2, ' ', 2),
        (3, ' ', 2),
    ]

    decodeData(example_data)