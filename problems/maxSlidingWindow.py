def solution(nums, k):
    if not nums:
        return nums

    ret = [max(nums[:k])]
    for i in range(1, len(nums) - k + 1):
        if nums[i + k - 1] >= ret[-1]:
            ret.append(nums[i + k - 1])
        elif nums[i - 1] < ret[-1]:
            ret.append(ret[-1])
        else:
            ret.append(max(nums[i:i + k]))
    return ret


print(solution([1, 3, -1, -3, 5, 3, 6, 7], 3))
