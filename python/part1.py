*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(trailing, current)
print('=' * 20)

from collections import deque
q = deque(maxlen=3)

q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)
q.appendleft(4)
q.pop()
q.popleft()
print('=' * 20)

import heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))  # Prints [42, 37, 23]
print(heapq.nsmallest(3, nums))  # Prints [-4, 1, 2]
print('=' * 20)

portfolio = [{
    'name': 'IBM',
    'shares': 100,
    'price': 91.1
}, {
    'name': 'AAPL',
    'shares': 50,
    'price': 543.22
}, {
    'name': 'FB',
    'shares': 200,
    'price': 21.09
}, {
    'name': 'HPQ',
    'shares': 35,
    'price': 31.75
}, {
    'name': 'YHOO',
    'shares': 45,
    'price': 16.35
}, {
    'name': 'ACME',
    'shares': 75,
    'price': 115.65
}]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
print(cheap)
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
print(expensive)
print('=' * 20)

import heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heap = list(nums)
heapq.heapify(heap)
print(heap)
print([heapq.heappop(heap) for i in range(3)])
print('=' * 20)

import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
print('=' * 20)

from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
print(d)
print('=' * 20)

d = {}  # 一个普通的字典
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)
print(d)
print('=' * 20)

from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
# Outputs "foo 1", "bar 2", "spam 3", "grok 4"
for key in d:
    print(key, d[key])
import json
print(json.dumps(d))
print('=' * 20)

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
min_price = min(zip(prices.values(), prices.keys()))
print(min_price)
# min_price is (10.75, 'FB')
max_price = max(zip(prices.values(), prices.keys()))
print(max_price)
# max_price is (612.78, 'AAPL')

prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)
# prices_sorted is [(10.75, 'FB'), (37.2, 'HPQ'),
#                   (45.23, 'ACME'), (205.55, 'IBM'),
#                   (612.78, 'AAPL')]
print('=' * 20)
# min_value = prices[min(prices, key=lambda k: prices[k])]

a = {'x': 1, 'y': 2, 'z': 3}

b = {'w': 10, 'x': 11, 'y': 2}

# Find keys in common
print(a.keys() & b.keys())  # { 'x', 'y' }
# Find keys in a that are not in b
print(a.keys() - b.keys())  # { 'z' }
# Find (key,value) pairs in common
print(a.items() & b.items())  # { ('y', 2) }
# Make a new dictionary with certain keys removed
c = {key: a[key] for key in a.keys() - {'z', 'w'}}
print(c)
# c is {'x': 1, 'y': 2}
print('=' * 20)


def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
print(list(dedupe(a, key=lambda d: (d['x'], d['y']))))
print('=' * 20)

record = '....................100 .......513.25 ..........'
SHARES = slice(20, 23)
PRICE = slice(31, 37)
cost = int(record[SHARES]) * float(record[PRICE])
print(cost)
a = slice(5, 50, 2)
s = 'HelloWorld'
print(a.indices(len(s)))
print('=' * 20)

from collections import Counter
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes', 'the', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't",
    'look', 'around', 'the', 'eyes', 'look', 'into', 'my', 'eyes', "you're",
    'under'
]
word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)

morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
for word in morewords:
    word_counts[word] += 1

print(word_counts['eyes'])
word_counts.update(morewords)
a = Counter(words)
b = Counter(morewords)
print(a + b)
print(a - b)
print('=' * 20)

rows = [{
    'fname': 'Brian',
    'lname': 'Jones',
    'uid': 1003
}, {
    'fname': 'David',
    'lname': 'Beazley',
    'uid': 1002
}, {
    'fname': 'John',
    'lname': 'Cleese',
    'uid': 1001
}, {
    'fname': 'Big',
    'lname': 'Jones',
    'uid': 1004
}]

from operator import itemgetter
rows_by_fname = sorted(rows, key=itemgetter('fname'))
print(rows_by_fname)

rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
print(rows_by_lfname)

rows_by_fname = sorted(rows, key=lambda r: r['fname'])
rows_by_lfname = sorted(rows, key=lambda r: (r['lname'], r['fname']))

print('=' * 20)


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


users = [User(23), User(3), User(99)]
print(users)
print(sorted(users, key=lambda u: u.user_id))

from operator import attrgetter
sorted(users, key=attrgetter('user_id'))
print('=' * 20)

rows = [
    {
        'address': '5412 N CLARK',
        'date': '07/01/2012'
    },
    {
        'address': '5148 N CLARK',
        'date': '07/04/2012'
    },
    {
        'address': '5800 E 58TH',
        'date': '07/02/2012'
    },
    {
        'address': '2122 N CLARK',
        'date': '07/03/2012'
    },
    {
        'address': '5645 N RAVENSWOOD',
        'date': '07/02/2012'
    },
    {
        'address': '1060 W ADDISON',
        'date': '07/02/2012'
    },
    {
        'address': '4801 N BROADWAY',
        'date': '07/01/2012'
    },
    {
        'address': '1039 W GRANVILLE',
        'date': '07/04/2012'
    },
]

from operator import itemgetter
from itertools import groupby

# Sort by the desired field first
# groupby() 仅仅检查连续的元素，如果事先并没有排序完成的话，分组函数将得不到想要的结果。
rows.sort(key=itemgetter('date'))
# Iterate in groups
# 每次迭代的时候，它会返回一个值和一个迭代器对
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ', i)

mylist = [1, 4, -5, 10, -7, 2, 3, -1]
print([n for n in mylist if n > 0])
pos = (n for n in mylist if n > 0)
for x in pos:
    print(x)
print('=' * 20)

values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False


ivals = list(filter(is_int, values))
print(ivals)
# Outputs ['1', '2', '-3', '4', '5']
print('=' * 20)

addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [0, 3, 10, 4, 1, 7, 6, 1]

from itertools import compress
more5 = [n > 5 for n in counts]
print(list(compress(addresses, more5)))
print('=' * 20)

from collections import namedtuple

Stock = namedtuple('Stock', ['name', 'shares', 'price'])
s = Stock('ACME', 100, 123.45)
print(s)
# 不像字典那样，一个命名元组是不可更改的
s = s._replace(shares=75)
print(s)
print('=' * 20)

# Data reduction across fields of a data structure
portfolio = [{
    'name': 'GOOG',
    'shares': 50
}, {
    'name': 'YHOO',
    'shares': 75
}, {
    'name': 'AOL',
    'shares': 20
}, {
    'name': 'SCOX',
    'shares': 65
}]
min_shares = min(s['shares'] for s in portfolio)
print(min_shares)
print('=' * 20)

from collections import ChainMap
c = ChainMap(a, b)
print(c['x'])  # Outputs 1 (from a)
print(c['y'])  # Outputs 2 (from b)
print(c['z'])  # Outputs 3 (from a)

values = ChainMap()
values['x'] = 1
print(values)
values = values.new_child()
values['x'] = 2
print(values)
values = values.parents
print(values)
print('=' * 20)
