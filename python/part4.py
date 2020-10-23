def manual_iter():
    with open('/etc/passwd') as f:
        try:
            while True:
                line = next(f)
                print(line, end='')
        except StopIteration:
            pass


with open('/etc/passwd') as f:
    while True:
        line = next(f, None)
        if line is None:
            break
        print(line, end='')
print('=' * 20)


class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)


root = Node(0)
child1 = Node(1)
child2 = Node(2)
root.add_child(child1)
root.add_child(child2)
# Outputs Node(1), Node(2)
for ch in root:
    print(ch)
print('=' * 20)


def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


for n in frange(0, 4, 0.5):
    print(n)
print('=' * 20)


class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()


# 深度优先方式遍历树形节点

root = Node(0)
child1 = Node(1)
child2 = Node(2)
root.add_child(child1)
root.add_child(child2)
child1.add_child(Node(3))
child1.add_child(Node(4))
child2.add_child(Node(5))

for ch in root.depth_first():
    print(ch)
# Outputs Node(0), Node(1), Node(3), Node(4), Node(2), Node(5)
print('=' * 20)


# 反方向迭代
class Countdown:
    def __init__(self, start):
        self.start = start

    # Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    # Reverse iterator
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1


for rr in Countdown(10):
    print(rr)
print('=' * 20)

from collections import deque


class linehistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


with open('/etc/passwd') as f:
    lines = linehistory(f)
    for line in lines:
        if 'admin' in line:
            for lineno, hline in lines.history:
                print('{}:{}'.format(lineno, hline), end='')
            print('-' * 20)
print('=' * 20)


# 迭代器生成的切片对象
def count(n):
    while True:
        yield n
        n += 1


c = count(0)
import itertools
for x in itertools.islice(c, 10, 20):
    print(x)
print('=' * 20)

items = ['a', 'b', 'c']
from itertools import permutations
for p in permutations(items):
    print(p)
print('-' * 20)

for p in permutations(items, 2):
    print(p)
print('-' * 20)

from itertools import combinations
for c in combinations(items, 3):
    print(c)
print('-' * 20)

from itertools import combinations_with_replacement
for c in combinations_with_replacement(items, 3):
    print(c)
print('=' * 20)

a = [1, 2, 3]
b = ['w', 'x', 'y', 'z']
for i in zip(a, b):
    print(i)
print('-' * 20)

from itertools import zip_longest
for i in zip_longest(a, b):
    print(i)
print('-' * 20)

for i in zip_longest(a, b, fillvalue=0):
    print(i)

headers = ['name', 'shares', 'price']
values = ['ACME', 100, 490.1]

# zip() 会创建一个迭代器来作为结果返回
print(dict(zip(headers, values)))
print(list(zip(a, b)))
print('=' * 20)

from itertools import chain
a = [1, 2, 3, 4]
b = ['x', 'y', 'z']
for x in chain(a, b):
    print(x)

print('=' * 20)

# 数据处理管道
import os
import fnmatch
import gzip
import bz2
import re


def gen_find(filepat, top):
    '''
    Find all filenames in a directory tree that match a shell wildcard pattern
    '''
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist, filepat):
            yield os.path.join(path, name)


def gen_opener(filenames):
    '''
    Open a sequence of filenames one at a time producing a file object.
    The file is closed immediately when proceeding to the next iteration.
    '''
    for filename in filenames:
        if filename.endswith('.gz'):
            f = gzip.open(filename, 'rt')
        elif filename.endswith('.bz2'):
            f = bz2.open(filename, 'rt')
        else:
            f = open(filename, 'rt')
        yield f
        f.close()


def gen_concatenate(iterators):
    '''
    Chain a sequence of iterators together into a single sequence.
    '''
    for it in iterators:
        # 将输入序列拼接成一个很长的行序列
        yield from it


def gen_grep(pattern, lines):
    '''
    Look for a regex pattern in a sequence of lines
    '''
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line


# lognames = gen_find('access-log*', 'www')
# files = gen_opener(lognames)
# lines = gen_concatenate(files)
# pylines = gen_grep('(?i)python', lines)
# for line in pylines:
#     print(line)

# lognames = gen_find('access-log*', 'www')
# files = gen_opener(lognames)
# lines = gen_concatenate(files)
# pylines = gen_grep('(?i)python', lines)
# bytecolumn = (line.rsplit(None, 1)[1] for line in pylines)
# bytes = (int(x) for x in bytecolumn if x != '-')
# print('Total', sum(bytes))

from collections import Iterable


def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)  #递归
        else:
            yield x


items = [1, 2, [3, 4, [5, 6], 7], 8]
# Produces 1 2 3 4 5 6 7 8
for x in flatten(items):
    print(x)
print('=' * 20)

import heapq
a = [1, 4, 7, 10]
b = [2, 5, 6, 11]
for c in heapq.merge(a, b):
    print(c)
print('=' * 20)

import sys
f = open('/etc/passwd')
# 不断调用 callable 对象直到返回值和标记值相等为止
for chunk in iter(lambda: f.read(10), ''):
    n = sys.stdout.write(chunk)