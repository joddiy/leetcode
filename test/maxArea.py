#O(n)
def solution(height):
    i, j = 0, len(height) - 1
    ret = min(height[j], height[i]) * (j - i)
    while i < j:
        ret = max(ret, min(height[i], height[j]) * (j - i))
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return ret


# print(solution([1, 8, 6, 2, 5, 4, 8, 3, 7]))
# print(solution([1, 1]))
print(solution([2, 3, 4, 5, 18, 17, 6]))
