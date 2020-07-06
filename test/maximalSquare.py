def solution(matrix):
    if not matrix or not matrix[0]:
        return 0

    dp = [[int(x) for x in row] for row in matrix]
    max_v = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == 0 or j == 0:
                max_v = max(max_v, dp[i][j])
            elif matrix[i][j] == "1":
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                max_v = max(max_v, dp[i][j])
            else:
                dp[i][j] == 0
    return max_v**2


print(
    solution([["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"],
              ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]))
