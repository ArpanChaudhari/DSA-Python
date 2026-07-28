from typing import List


def equalPairs(grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    rows_map = {}
    count = 0

    for i in range(m):
        key = tuple(grid[i])
        rows_map[key] = rows_map.get(key, 0) + 1

    for j in range(m):
        # column = []

        # for i in range(n):
        #     column.append(grid[i][j])

        # key = tuple(column)

        key = tuple(grid[i][j] for i in range(n))
        count += rows_map.get(key, 0)

    return count


# grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
grid = [[1, 1], [1, 1]]
print(equalPairs(grid))
