def solution(heights):
    heights = [0] + heights + [0]
    n = len(heights)
    min_left = [0] * n
    min_right = [0] * n
    ret = 0
    for i in range(1, n - 1):
        tmp_i = i - 1
        while tmp_i > 0 and heights[tmp_i] >= heights[i]:
            tmp_i = min_left[tmp_i]
        min_left[i] = tmp_i
    for j in range(n - 2, 0, -1):
        tmp_j = j + 1
        while tmp_j < n - 1 and heights[tmp_j] >= heights[j]:
            tmp_j = min_right[tmp_j]
        min_right[j] = tmp_j
    for i in range(1, n - 1):
        ret = max(ret, heights[i] * (min_right[i] - min_left[i] - 1))
    return ret


print(solution([2, 1, 5, 6, 2, 3]))
