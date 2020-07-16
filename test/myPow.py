def solutin(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    if n < 0:
        sign = -1
        n = -n
    else:
        sign = 1
    res = n % 2
    half = solutin(x, n // 2)
    ret = half * half if res == 0 else half * half * x
    if sign < 0:
        ret = 1 / ret
    return ret


# print(solutin(2., 10))
# print(solutin(2., 2))
print(solutin(2., -2))
print(solutin(2., 0))