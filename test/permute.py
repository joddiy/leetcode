def solution(nums):
    ret = []
    n = len(nums)

    def recursion(prefix, remaining):
        if not remaining:
            ret.append(prefix)
        else:
            for k in range(len(remaining)):
                recursion(prefix+[remaining[k]], remaining[:k] + remaining[k+1:])
    recursion([], nums)
    return ret


print(solution([1, 2, 3]))
