def solution(strs):
    ret = ""
    j = 0
    while True:
        cur_c = ""
        for i in range(len(strs)):
            s = strs[i]
            if j >= len(s):
                return ret
            c = s[j]
            if not cur_c:
                cur_c = c
            elif c != cur_c:
                return ret
        j += 1
        ret += cur_c


print(solution(["flower", "flow", "flight"]))
print(solution(["dog", "racecar", "car"]))
print(solution(["d", "d", "d"]))
print(solution(["", "", ""]))
print(solution([""]))
