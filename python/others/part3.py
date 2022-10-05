print(round(1.23, 1))
print(round(1.15, 1))
print(round(162, -1))
print(format(1.23456, '0.2f'))
print('=' * 20)

print(4.2 + 2.1)
from decimal import Decimal
print(Decimal('4.2') + Decimal('2.1'))

from decimal import localcontext
a = Decimal('1.3')
b = Decimal('1.7')
print(a / b)

with localcontext() as ctx:
    ctx.prec = 3
    print(a / b)

with localcontext() as ctx:
    ctx.prec = 50
    print(a / b)

nums = [1.23e+18, 1, -1.23e+18]
print(sum(nums))
import math
print(math.fsum(nums))
print('=' * 20)

x = 1234.56789
print(format(x, '0.2f'))
print(format(x, '>10.1f'))
print(format(x, '^10.1f'))
print(format(x, ','))
print(format(x, ',.1f'))
print(format(x, 'e'))
print(format(x, '0.2E'))
print('=' * 20)

x = 1234
print(bin(x))
print(oct(x))
print(hex(x))
print(format(x, 'b'))
print(format(x, 'o'))
print(format(x, 'x'))
x = -1234
print(format(2**32 + x, 'b'))
print(format(2**32 + x, 'x'))
print(int('4d2', 16))
print(int('10011010010', 2))
# import os
# os.chmod('script.py', 0o755)
print('=' * 20)

data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
print(int.from_bytes(data, 'little'))
print(int.from_bytes(data, 'big'))
x = 94522842520747284487117727783387188
print(x.to_bytes(16, 'big'))
print(x.to_bytes(16, 'little'))
x = 0x01020304
print(x.to_bytes(4, 'big'))
print(x.to_bytes(4, 'little'))

x = 523**23
nbytes, rem = divmod(x.bit_length(), 8)
if rem:
    nbytes += 1
print(x.to_bytes(nbytes, 'little'))
print('=' * 20)

print(complex(2, 4))
print(3 - 5j)

a = complex(2, 4)
print(a.real, a.imag, a.conjugate)
import cmath
print(cmath.sin(a))
print(cmath.cos(a))
print(cmath.exp(a))
print(cmath.sqrt(-1))
print('=' * 20)

print(float('inf'))
print(float('-inf'))
print(float('nan'))
math.isinf(float('inf'))
math.isnan(float('nan'))
c = float('nan')
d = float('nan')
# NaN值的一个特别的地方时它们之间的比较操作总是返回False
print(c == d)
print(c is d)
print('=' * 20)

from fractions import Fraction
a = Fraction(5, 4)
b = Fraction(7, 16)
print(a + b)
print(a * b)
c = a * b
print(c.numerator)
print(c.denominator)

# Limiting the denominator of a value
print(c.limit_denominator(8))

# Converting a float to a fraction
x = 3.75
y = Fraction(*x.as_integer_ratio())
print(y)
print('=' * 20)

import random
values = [1, 2, 3, 4, 5, 6]
for _ in range(5):
    print(random.choice(values))
print(random.sample(values, 3))
random.shuffle(values)
print(values)
print(random.randint(0, 10))
print(random.random())
print(random.getrandbits(200))

random.seed()  # Seed based on system time or os.urandom()
random.seed(12345)  # Seed based on integer given
random.seed(b'bytedata')  # Seed based on byte data

print(random.uniform(0, 1))
print(random.gauss(0, 1))
print('=' * 20)

from datetime import timedelta

a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b
print(c.days)
print(c.seconds)
print(c.seconds / 3600)
print(c.total_seconds() / 3600)

from datetime import datetime

a = datetime(2012, 9, 23)
print(a + timedelta(days=10))
b = datetime(2012, 12, 21)
d = b - a
print(d.days)
now = datetime.today()
print(now)
print(now + timedelta(minutes=10))
print('=' * 20)

from datetime import datetime, timedelta

weekdays = [
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
    'Sunday'
]


def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date


print(datetime.today())  # For reference
print(get_previous_byday('Monday'))
print(get_previous_byday('Tuesday'))  # Previous week, not today
print(get_previous_byday('Friday'))
print('=' * 20)

from datetime import datetime, date, timedelta
import calendar


def get_month_range(start_date=None):
    if start_date is None:
        start_date = date.today().replace(day=1)
    _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    end_date = start_date + timedelta(days=days_in_month)
    return (start_date, end_date)


a_day = timedelta(days=1)
first_day, last_day = get_month_range()
while first_day < last_day:
    print(first_day)
    first_day += a_day
print('=' * 20)

text = '2012-09-20'
y = datetime.strptime(text, r'%Y-%m-%d')
z = datetime.now()
diff = z - y
print(diff)