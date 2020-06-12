def solution(nums, target):
    if not nums:
        return -1

    def recursion(i, j):
        if j < i:
            return -1
        m = (i+j)//2
        if nums[m] == target:
            return m
        # target locates at non-axis side (and is left side)
        elif nums[i] <= target < nums[m]:
            return recursion(i, m-1)
        # target locates at non-axis side (and is right side)
        elif nums[m] < target <= nums[j]:
            return recursion(m+1, j)
        # target locates at axis side (and is right side)
        elif nums[m] > nums[j]:
            return recursion(m+1, j)
        # target locates at axis side (and is left side)
        else:
            return recursion(i, m-1)
    return recursion(0, len(nums)-1)


print(solution([4, 5, 6, 7, 0, 1, 2], 0))
