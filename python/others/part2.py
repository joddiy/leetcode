import re
line = 'asdf fjdk; afed, fjek,asdf, foo'
print(re.split(r'[;,\s]\s*', line))
# 括号捕获分组
print(re.split(r'(;|,|\s)\s*', line))
# 非捕获分组
print(re.split(r'(?:;|,|\s)\s*', line))
print('=' * 20)

import os
filenames = ['Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h']
print([name for name in filenames if name.endswith(('.c', '.h'))])
print(any(name.endswith('.py') for name in filenames))
# startswith 必须用元组作为参数
print('=' * 20)

from fnmatch import fnmatch, fnmatchcase
print(fnmatch('foo.txt', '*.TXT'))
print(fnmatchcase('foo.txt', '*.TXT'))

addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]
print(
    [addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')])
# fnmatch() 函数匹配能力介于简单的字符串方法和强大的正则表达式之间
print('=' * 20)

import re
text1 = '11/27/2012'
datepat = re.compile(r'\d+/\d+/\d+')
print(datepat.match(text1))
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(datepat.findall(text))

#利用括号去捕获分组
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/27/2012')
print(m.groups())
datepat.findall(text)
for month, day, year in datepat.findall(text):
    print('{}-{}-{}'.format(year, month, day))
for m in datepat.finditer(text):
    print('{}-{}-{}'.format(*m.groups()))
print('=' * 20)

text = 'yeah, but no, but yeah, but no, but yeah'
print(text.replace('yeah', 'yep'))
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.sub(r'\3-\1-\2', text))

print(
    re.sub(r'(?P<month>\d+)/(?P<day>\d+)/(?P<year>\d+)',
           r'\g<year>-\g<month>-\g<day>', text))

from calendar import month_abbr


def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))


print(datepat.sub(change_date, text))
# 忽略大小写
text = 'UPPER PYTHON, lower python, Mixed Python'
re.findall('python', text, flags=re.IGNORECASE)
print('=' * 20)

# 贪婪的, 最长可能匹配
str_pat = re.compile(r'"(.*)"')
text2 = 'Computer says "no." Phone says "yes."'
print(str_pat.findall(text2))

# 非贪婪模式, 最短的匹配
str_pat = re.compile(r'"(.*?)"')
print(str_pat.findall(text2))
print('=' * 20)

# 跨行匹配, 点(.)不能匹配换行符
comment = re.compile(r'/\*(.*?)\*/')
text2 = '''/* this is a
    multiline comment */
    '''
print(comment.findall(text2))
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment.findall(text2))

# 标志参数, re.DOTALL
comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
print(comment.findall(text2))
print('=' * 20)

s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
print(s1, s2, s1 == s2)

# NFC表示字符应该是整体组成(比如可能的话就使用单一编码)
# 而NFD表示字符应该分解为多个组合字符表示
# 同样支持扩展的标准化形式NFKC和NFKD

import unicodedata
t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print(t1 == t2)

t3 = unicodedata.normalize('NFD', s1)
t4 = unicodedata.normalize('NFD', s2)
print(t1 == t2)

# 清除掉一些文本上面的变音符的时候
t1 = unicodedata.normalize('NFD', s1)
print(''.join(c for c in t1 if not unicodedata.combining(c)))
print(t1 == t2)

num = re.compile(r'\d+')
print(num.match('\u0661\u0662\u0663'))

pat = re.compile('stra\u00dfe', re.IGNORECASE)
s = 'straße'
print(pat.match(s))  # Matches
print(pat.match(s.upper()))
print(s.upper())
print('=' * 20)

# Whitespace stripping
s = ' hello world \n'
print(s.strip())
print(s.lstrip())
print(s.rstrip())
# Character stripping
t = '-----hello====='
print(t.lstrip('-'))
print(t.strip('-='))
s = s.strip()
print(s.replace(r'\s+', ''))
print(re.sub(r'\s+', ' ', s))
print('=' * 20)

s = 'pýtĥöñ\fis\tawesome\r\n'
remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None  # Deleted
}
a = s.translate(remap)
print(a)

import unicodedata
import sys
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode)
                         if unicodedata.combining(chr(c)))

b = unicodedata.normalize('NFD', a)
print(b.translate(cmb_chrs))

digitmap = {
    c: ord('0') + unicodedata.digit(chr(c))
    for c in range(sys.maxunicode) if unicodedata.category(chr(c)) == 'Nd'
}

# Arabic digits
x = '\u0661\u0662\u0663'
print(x.translate(digitmap))
b = unicodedata.normalize('NFD', a)
print(b.encode('ascii', 'ignore').decode('ascii'))
print('=' * 20)

text = 'Hello World'
print(text.ljust(20))
print(text.rjust(20))
print(text.center(20))
print(text.rjust(20, '='))
print(text.center(20, '*'))
print(format(text, '>20'))
print(format(text, '<20'))
print(format(text, '^20'))
print(format(text, '=>20s'))
print(format(text, '*^20s'))
'{:>10s} {:>10s}'.format('Hello', 'World')
x = 1.2345
print(format(x, '>10'))
print(format(x, '^10.2f'))
print('=' * 20)

s = '{name} has {n} messages.'
print(s.format(name='Guido', n=37))

name = 'Guido'
n = 37
print(s.format_map(vars()))


class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n


a = Info('Guido', 37)
print(s.format_map(vars(a)))


class safesub(dict):
    """防止key找不到"""
    def __missing__(self, key):
        return '{' + key + '}'


import sys


def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))


name = 'Guido'
n = 37
print(sub('Hello {name}'))
print(sub('You have {n} messages.'))
print(sub('Your favorite color is {color}'))

s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."

import textwrap
print(textwrap.fill(s, 70))
print(textwrap.fill(s, 40))
print(textwrap.fill(s, 40, initial_indent='    '))
print(textwrap.fill(s, 40, subsequent_indent='    '))

import os
print(os.get_terminal_size().columns)
print(textwrap.fill(s, os.get_terminal_size().columns, initial_indent='    '))

s = 'Elements are written as "<tag>text</tag>".'
import html
print(s)
print(html.escape(s))
print('=' * 20)
s = 'Spicy Jalapeño'
print(s.encode('ascii', errors='xmlcharrefreplace'))
s = 'Spicy &quot;Jalape&#241;o&quot.'
from html.parser import HTMLParser
p = HTMLParser()
print(p.unescape(s))
t = 'The prompt is &gt;&gt;&gt;'
from xml.sax.saxutils import unescape
print(unescape(t))

print('=' * 20)
text = 'foo = 23 + 42 * 10'
tokens = [('NAME', 'foo'), ('EQ', '='), ('NUM', '23'), ('PLUS', '+'),
          ('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]

import re
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))
scanner = master_pat.scanner('foo = 42')
for m in iter(scanner.match, None):
    print(m.lastgroup, m.group())

from collections import namedtuple


def generate_tokens(pat, text):
    Token = namedtuple('Token', ['type', 'value'])
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())


# Example use
for tok in generate_tokens(master_pat, 'foo = 42'):
    print(tok)
print('=' * 20)

data = b'Hello World'
data = bytearray(b'Hello World')
data = b'FOO:BAR,SPAM'
print(re.split(b'[:,]', data))  # Notice: pattern as bytes

# 字节字符串的索引操作返回整数而不是单独字符
b = b'Hello World'  # Byte string
print(b[0])
