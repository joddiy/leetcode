def solution(height):
    height = [0] + height + [0]
    n = len(height)
    ret = 0
    max_left = [0] * n  # record the max height from left
    max_right = [0] * n  # record the max height from right
    cur_max = height[0]
    for i in range(n):
        cur_max = max(cur_max, height[i])
        max_left[i] = cur_max
    cur_max = height[-1]
    for i in range(n - 1, -1, -1):
        cur_max = max(cur_max, height[i])
        max_right[i] = cur_max
        ret += min(max_left[i], max_right[i]) - height[i]
    return ret


print(solution([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
