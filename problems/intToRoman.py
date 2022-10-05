def solutin(num):
    pos = ["I", "V", "X", "L", "C", "D", "M"]

    idx = 0
    ret = []
    while num != 0:
        tmp = ""
        res = num % 10
        num = num // 10
        if res == 9:
            tmp += pos[idx] + pos[idx + 2]
        elif res == 4:
            tmp += pos[idx] + pos[idx + 1]
        else:
            if res >= 5:
                tmp += pos[idx + 1]
                res = res % 5
            tmp += pos[idx] * res
        ret.append(tmp)
        idx += 2
    return "".join(ret[::-1])


# print(solutin(3))
# print(solutin(4))
# print(solutin(9))
# print(solutin(13))
# print(solutin(14))
print(solutin(8))
print(solutin(58))
# print(solutin(1994))