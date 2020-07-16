def solution(nums, k):
    nums[::] = nums[-k:] + nums[:-k]
    return nums


print(solution([1, 2, 3, 4, 5, 6, 7], 3))
