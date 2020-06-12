import sys

# O(n)


def solution(nums):
    cur_sum = 0
    max_v = -sys.maxsize
    for num in nums:
        cur_sum = max(0, cur_sum) + num
        max_v = max(max_v, cur_sum)
    return max_v


print(solution([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
# print(solution([1]))
# print(solution([-1]))
# print(solution([-2, -1]))
# print(solution([1, 2]))
