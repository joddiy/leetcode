def solution(n):
    ret = []
    if n == 0:
        return ret

    def recursion(prefix, i, j):
        # i means the assigned number of "(" and don't have ")"
        # j means the available number of "("
        if i == 0 and j == 0:
            ret.append(prefix)
        elif i == 0:
            recursion(prefix + "(", i + 1, j - 1)
        elif j == 0:
            recursion(prefix + ")", i - 1, j)
        else:
            recursion(prefix + "(", i + 1, j - 1)
            recursion(prefix + ")", i - 1, j)

    recursion("", 0, n)
    return ret


print(solution(3))
