def solution(nums):
    n = len(nums)
    ret = []

    def recursion(prefix, i):
        ret.append(prefix)
        for j in range(i, n):
            recursion(prefix + [nums[j]], j + 1)

    recursion([], 0)
    return ret


print(solution([1, 2, 3]))
print(solution([]))