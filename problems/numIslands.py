def solution(grid):
    if not len(grid) or not len(grid[0]):
        return 0
    ret = 0
    n = len(grid)
    m = len(grid[0])
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "1":
                grid[i][j] = "0"
                ret += 1
                queue = [(i, j)]
                while queue:
                    _i, _j = queue.pop(0)
                    if _i > 0 and grid[_i - 1][_j] == "1":
                        grid[_i - 1][_j] = "0"
                        queue.append((_i - 1, _j))
                    if _j > 0 and grid[_i][_j - 1] == "1":
                        grid[_i][_j - 1] = "0"
                        queue.append((_i, _j - 1))
                    if _i < n - 1 and grid[_i + 1][_j] == "1":
                        grid[_i + 1][_j] = "0"
                        queue.append((_i + 1, _j))
                    if _j < m - 1 and grid[_i][_j + 1] == "1":
                        grid[_i][_j + 1] = "0"
                        queue.append((_i, _j + 1))
    return ret


# print(
#     solution([["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"],
#               ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]))
print(
    solution([["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"],
              ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]))
