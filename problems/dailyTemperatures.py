def solution(T):
    ret = [0] * len(T)
    stack = [(T[0], 0)]
    for i in range(1, len(T)):
        top = stack[-1]
        if T[i] > top[0]:
            while stack and T[i] > stack[-1][0]:
                _t = stack.pop()
                ret[_t[1]] = i - _t[1]
        stack.append((T[i], i))
    return ret

# print(solution([73, 74, 75, 71, 69, 72, 76, 73]))
print(solution([73]))