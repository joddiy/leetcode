def solution(matrix):
    if not matrix:
        return 0
    m, n = len(matrix), len(matrix[0])
    left, right, height = [0] * n, [n] * n, [0] * n
    max_v = 0
    for i in range(m):
        cur_left, cur_right = 0, n
        for j in range(n):
            if matrix[i][j] == '1':
                height[j] += 1
                left[j] = max(left[j], cur_left)
            else:
                height[j] = 0
                left[j] = 0
                cur_left = j + 1
            j = n - j - 1
            if matrix[i][j] == '1':
                right[j] = min(right[j], cur_right)
            else:
                right[j] = n
                cur_right = j
        for j in range(n):
            max_v = max(max_v, (right[j] - left[j]) * height[j])
    return max_v


print(
    solution([["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"],
              ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]))
print(solution([["1"]]))