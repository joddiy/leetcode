def solution(s):
    s = s[::-1]
    i = 0
    hash_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    cur_base = 0
    ret = 0
    for c in s:
        num = hash_map[c]
        if num < cur_base:
            ret -= num
        else:
            ret += num
        cur_base = num
    return ret


print(solution("III"))
print(solution("IV"))
print(solution("IX"))
print(solution("LVIII"))