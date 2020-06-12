def solution(matrix):
    n = len(matrix)
    i, j = 0, n - 1
    # swap
    while i < j:
        matrix[i], matrix[j] = matrix[j], matrix[i]
        i += 1
        j -= 1
    # transpose
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix


print(solution([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
],))
