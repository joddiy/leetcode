def solution(candidates, target):
    ret = []

    def recursion(prefix, i, target):
        if target == 0:
            ret.append(prefix)
        for i in range(i, len(candidates)):
            num = candidates[i]
            if target - num >= 0:
                recursion(prefix + [num], i, target - num)

    recursion([], 0, target)
    return ret


print(solution([2, 3, 6, 7], 7))
