import sys


def solutin(x):
    sign = -1 if x < 0 else 1
    x = abs(x)
    y = 0
    while x != 0:
        res = x % 10
        x = x // 10
        y = y * 10 + res
    y *= sign
    return 0 if abs(y) > 0x7FFFFFFF else y


print(solutin(123))
print(solutin(-123))
print(solutin(120))