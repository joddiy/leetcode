def solution(triangle):
    # dp[0,0] = max(dp[1,0], dp[1,1]) + triangle[0, 0]
    # dp[i, j] = max(dp[i+1, j], dp[i+1, j+1]) + triangle[i, j]
    # dp[n, j] = triangle[n, j]
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
    return triangle[0][0]

print(solution([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
