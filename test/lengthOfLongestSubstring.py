# O(kn)
def solution(a):
    i, j = 0, 0
    indice = {}
    ret = 0
    while j < len(a):
        if a[j] in indice:
            i = indice[a[j]]
            # reconstruct the indice map
            indice = {a[k]: k for k in range(i+1, j+1)}
        else:
            # only add the current element
            indice[a[j]] = j
        ret = max(ret, len(indice))
        j += 1
    return ret

# O(n)
def solution2(a):
    i, j = 0, 0
    indice = {}
    ret = 0
    while j < len(a):
        if a[j] in indice:
            # once we find a duplicate key
            # then valid path must be the length between these two key minus 1
            i = max(indice[a[j]], i)
        ret = max(ret, j-i+1)
        indice[a[j]] = j+1
        j += 1
    return ret


print(solution2("abcabcbb"))
