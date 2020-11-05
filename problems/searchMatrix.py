def solution(matrix, target):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return False
    j = len(matrix[0]) - 1
    for i in range(len(matrix)):
        while j >= 0 and matrix[i][j] > target:
            j -= 1
        if matrix[i][j] == target:
            return True
    return False


matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22],
          [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
# print(solution(matrix, 5))
print(solution(matrix, 20))