def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))


# Sample use
print(avg(1, 2))  # 1.5
print(avg(1, 2, 3, 4))  # 2.5


def anyargs(*args, **kwargs):
    print(args)  # A tuple
    print(kwargs)  # A dict


print(anyargs(1, 2, key1=1, key2=2))

print('=' * 20)


def recv(maxsize, *, block):
    'Receives a message'
    pass


# recv(1024, True) # TypeError
recv(1024, block=True)  # Ok


def add(x: int, y: int) -> int:
    return x + y


# 实际上我们使用的是逗号来生成一个元组，而不是用括号
a = (1, 2)  # With parentheses
b = 1, 2  # Without parentheses

_no_value = object()


# _no_value 唯一，用户不可能传递
# 达到区分效果
def spam(a, b=_no_value):
    if b is _no_value:
        print('No b value supplied')


# 不可使用可变对象，因为默认值在函数定义的时候就已经确定了
def spam(a, b=[]):
    print(b)
    return b


add = lambda x, y: x + y
add(2, 3)

names = ['David Beazley', 'Brian Jones', 'Raymond Hettinger', 'Ned Batchelder']
print(sorted(names, key=lambda name: name.split()[-1].lower()))

# 运行时绑定值
x = 10
a = lambda y: x + y
x = 20
b = lambda y: x + y
print(a(10))  # 30
print(b(10))  # 30

# 定义时就捕获到值

x = 10
a = lambda y, x=x: x + y
x = 20
b = lambda y, x=x: x + y
print(a(10))  # 30
print(b(10))  # 30

funcs = [lambda x: x + n for n in range(5)]
for f in funcs:
    print(f(0))  # 4,4,4,4,4

funcs = [lambda x, n=n: x + n for n in range(5)]
for f in funcs:
    print(f(0))  # 0,1,2,3,4

print('=' * 20)


def spam(a, b, c, d):
    print(a, b, c, d)


# partial() 函数允许你给一个或多个参数设置固定的值

from functools import partial
s1 = partial(spam, 1)  # a = 1
s1(2, 3, 4)
s1(4, 5, 6)
s2 = partial(spam, d=42)  # d = 42
s2(1, 2, 3)
s2(4, 5, 5)
s3 = partial(spam, 1, 2, d=42)  # a = 1, b = 2, d = 42

points = [(1, 2), (3, 4), (5, 6), (7, 8)]

# 使用闭包来将单个方法的类转换成函数
from urllib.request import urlopen


# 内部函数里用外部函数的参数，从而记住
def urltemplate(template):
    def opener(**kwargs):
        return urlopen(template.format_map(kwargs))

    return opener


def output_result(result, log=None):
    if log is not None:
        log.debug('Got: %r', result)


# A sample function
def add(x, y):
    return x + y


import logging
from multiprocessing import Pool
from functools import partial

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('test')

p = Pool()
p.apply_async(add, (3, 4), callback=partial(output_result, log=log))
p.close()
p.join()

# 很多时候 partial() 能实现的效果，lambda表达式也能实现
# p.apply_async(add, (3, 4), callback=lambda result: output_result(result,log))

print('=' * 20)


# 给回调函数传参数
def apply_async(func, args, *, callback):
    # Compute the result
    result = func(*args)

    # Invoke the callback with the result
    callback(result)


def print_result(result):
    print('Got:', result)


def add(x, y):
    return x + y


apply_async(add, (2, 3), callback=print_result)

# 使用一个绑定方法来代替一个简单函数


class ResultHandler:
    def __init__(self):
        self.sequence = 0

    def handler(self, result):
        self.sequence += 1
        print('[{}] Got: {}'.format(self.sequence, result))


r = ResultHandler()
apply_async(add, (2, 3), callback=r.handler)


# 包捕获状态值
def make_handler():
    sequence = 0

    def handler(result):
        nonlocal sequence
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))

    return handler


handler = make_handler()
apply_async(add, (2, 3), callback=handler)

# 协程
# def make_handler():
#     sequence = 0
#     while True:
#         result = yield
#         sequence += 1
#         print('[{}] Got: {}'.format(sequence, result))

# handler = make_handler()
# next(handler) # Advance to the yield
# apply_async(add, (2, 3), callback=handler.send)

print('=' * 20)


# 访问闭包中定义的变量
# 闭包的方案运行起来要快大概8%
# 大部分原因是因为对实例变量的简化访问
# 闭包更快是因为不会涉及到额外的self变量
def sample():
    n = 0

    # Closure function
    def func():
        print('n=', n)

    # Accessor methods for n
    def get_n():
        return n

    def set_n(value):
        nonlocal n
        n = value

    # Attach as function attributes
    func.get_n = get_n
    func.set_n = set_n
    return func


f = sample()
f()
f.set_n(10)
print(f.get_n())