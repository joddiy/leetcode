def solution(nums):
    n = len(nums)
    i, j, k = 0, 0, n - 1
    while i <= k:
        if nums[i] == 0:
            if i != j:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
            else:
                j += 1
                i += 1
        elif nums[i] == 2:
            nums[i], nums[k] = nums[k], nums[i]
            k -= 1
        else:
            i += 1
    return nums


print(solution([2, 0, 2, 1, 1, 0]))
print(solution([1, 2, 0]))
