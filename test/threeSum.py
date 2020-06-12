# O(n^2) sort
def solution(nums):
    n = len(nums)
    nums.sort()
    ret = []
    for i in range(n-2):
        if i > 0 and nums[i] == nums[i-1]: # avoid repeat
            continue
        j, k = i+1, n-1
        while j < k:
            s = nums[i] + nums[j] + nums[k]
            if s < 0:
                j += 1
            elif s > 0:
                k -= 1
            else:
                ret.append([nums[i], nums[j], nums[k]])
                while j < k and nums[j] == nums[j+1]: # avoid repeat
                    j += 1
                while j < k and nums[k] == nums[k-1]: # avoid repeat
                    k -= 1
                j += 1
                k -= 1
    return ret


# print(solution([-1, 0, 1, 2, -1, -4]))
# print(solution([1, 2, -2, -1]))
print(solution([-1, 0, 1, 0]))
