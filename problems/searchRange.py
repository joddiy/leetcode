def solution(nums, target):

    def recursion_left(s, e):
        if e < s:
            return s
        m = (s + e) // 2
        if nums[m] < target:
            return recursion_left(m + 1, e)
        else:
            return recursion_left(s, m - 1)

    def recursion_right(s, e):
        if e < s:
            return e
        m = (s + e) // 2
        if nums[m] <= target:
            return recursion_right(m + 1, e)
        else:
            return recursion_right(s, m - 1)

    left = recursion_left(0, len(nums) - 1)
    right = recursion_right(0, len(nums) - 1)
    print(left, right)
    if left > right:
        return [-1, -1]
    else:
        return [left, right]


print(solution([5, 7, 7, 8, 8, 10], 8))
