import csv
with open('./tmp/stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        print(row)

print('=' * 20)

from collections import namedtuple
with open('./tmp/stocks.csv') as f:
    f_csv = csv.reader(f)
    headings = next(f_csv)
    Row = namedtuple('Row', headings)
    for r in f_csv:
        row = Row(*r)
        print(row)

print('=' * 20)

import csv
with open('./tmp/stocks.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        print(row)

print('=' * 20)

# 写入
headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
rows = [
    ('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
    ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
    ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
]

with open('./tmp/stocks.csv', 'w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)

headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
rows = [
    {
        'Symbol': 'AA',
        'Price': 39.48,
        'Date': '6/11/2007',
        'Time': '9:36am',
        'Change': -0.18,
        'Volume': 181800
    },
    {
        'Symbol': 'AIG',
        'Price': 71.38,
        'Date': '6/11/2007',
        'Time': '9:36am',
        'Change': -0.15,
        'Volume': 195500
    },
    {
        'Symbol': 'AXP',
        'Price': 62.58,
        'Date': '6/11/2007',
        'Time': '9:36am',
        'Change': -0.46,
        'Volume': 935000
    },
]

with open('./tmp/stocks.csv', 'w') as f:
    f_csv = csv.DictWriter(f, headers)
    f_csv.writeheader()
    f_csv.writerows(rows)

# Example of reading tab-separated values
# with open('stock.tsv') as f:
#     f_tsv = csv.reader(f, delimiter='\t')
#     for row in f_tsv:
#         print(row)

import json

data = {'name': 'ACME', 'shares': 100, 'price': 542.23}

# Writing JSON data
with open('./tmp/data.json', 'w') as f:
    json.dump(data, f)

# Reading data back
with open('./tmp/data.json', 'r') as f:
    data = json.load(f)

print('=' * 20)

from pprint import pprint

with open('./tmp/data.json', 'r') as f:
    data = json.load(f)
    pprint(data)

s = '{"name": "ACME", "shares": 50, "price": 490.1}'
from collections import OrderedDict
data = json.loads(s, object_pairs_hook=OrderedDict)
print(data)


class JSONObject:
    def __init__(self, d):
        self.__dict__ = d


data = json.loads(s, object_hook=JSONObject)
print(data.name)

data = {'name': 'ACME', 'shares': 100, 'price': 542.23}
print(json.dumps(data))
print(json.dumps(data, indent=4))


# 序列化对象实例
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def serialize_instance(obj):
    d = {'__classname__': type(obj).__name__}
    d.update(vars(obj))
    return d


# Dictionary mapping names to known classes
classes = {'Point': Point}


def unserialize_object(d):
    clsname = d.pop('__classname__', None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls)  # Make instance without calling __init__
        for key, value in d.items():
            setattr(obj, key, value)
        return obj
    else:
        return d


p = Point(2, 3)
s = json.dumps(p, default=serialize_instance)
print(s)
a = json.loads(s, object_hook=unserialize_object)
print(a)

print('=' * 20)

# from urllib.request import urlopen
# from xml.etree.ElementTree import parse

# # Download the RSS feed and parse it
# u = urlopen('http://planet.python.org/rss20.xml')
# doc = parse(u)

# # Extract and output tags of interest
# for item in doc.iterfind('channel/item'):
#     title = item.findtext('title')
#     date = item.findtext('pubDate')
#     link = item.findtext('link')

#     print(title)
#     print(date)
#     print(link)
#     print()

print('=' * 20)

# from xml.etree.ElementTree import iterparse

# # 增量式解析
# def parse_and_remove(filename, path):
#     path_parts = path.split('/')
#     doc = iterparse(filename, ('start', 'end'))
#     # Skip the root element
#     next(doc)

#     tag_stack = []
#     elem_stack = []
#     # 一种或多种类型的事件列表: start, end, start-ns 和 end-ns
#     for event, elem in doc:
#         if event == 'start':
#             tag_stack.append(elem.tag)
#             elem_stack.append(elem)
#         elif event == 'end':
#             if tag_stack == path_parts:
#                 yield elem
#                  # 从父节点中删除已经访问过得节点
#                 elem_stack[-2].remove(elem)
#             try:
#                 tag_stack.pop()
#                 elem_stack.pop()
#             except IndexError:
#                 pass

# from collections import Counter

# potholes_by_zip = Counter()

# data = parse_and_remove('potholes.xml', 'row/row')
# for pothole in data:
#     potholes_by_zip[pothole.findtext('zip')] += 1
# for zipcode, num in potholes_by_zip.most_common():
#     print(zipcode, num)

print('=' * 20)

from xml.etree.ElementTree import Element


def dict_to_xml(tag, d):
    '''
    Turn a simple dict of key/value pairs into XML
    '''
    elem = Element(tag)
    for key, val in d.items():
        child = Element(key)
        child.text = str(val)
        elem.append(child)
    return elem


s = {'name': 'GOOG', 'shares': 100, 'price': 490.1}
e = dict_to_xml('stock', s)

from xml.etree.ElementTree import tostring
print(tostring(e))
e.set('_id', '1234')
print(tostring(e))

from xml.sax.saxutils import escape, unescape
_ = escape('<spam>')
print(_)
print(unescape(_))

print('=' * 20)

from xml.etree.ElementTree import parse, Element
doc = parse('./tmp/pred.xml')
root = doc.getroot()
print(root)
# Remove a few elements
root.remove(root.find('sri'))
root.remove(root.find('cr'))
e = Element('spam')
e.text = 'This is a test'
root.insert(2, e)
# Write back to a file
doc.write('./tmp/newpred.xml', xml_declaration=True)

print('=' * 20)


class XMLNamespaces:
    def __init__(self, **kwargs):
        self.namespaces = {}
        for name, uri in kwargs.items():
            self.register(name, uri)

    def register(self, name, uri):
        self.namespaces[name] = '{' + uri + '}'

    def __call__(self, path):
        return path.format_map(self.namespaces)


ns = XMLNamespaces(html='http://www.w3.org/1999/xhtml')

print(ns('content/{html}html'))

print('=' * 20)

stocks = [
    ('GOOG', 100, 490.1),
    ('AAPL', 50, 545.75),
    ('FB', 150, 7.45),
    ('HPQ', 75, 33.2),
]

import sqlite3
with sqlite3.connect('./tmp/database.db') as db:
    c = db.cursor()
    # c.execute('create table portfolio (symbol text, shares integer, price real)')
    # db.commit()
    # c.executemany('insert into portfolio values (?,?,?)', stocks)
    # db.commit()
    for row in db.execute('select * from portfolio'):
        print(row)

print('=' * 20)

# 编码和解码十六进制数
# 大小写
s = b'hello'
import binascii
h = binascii.b2a_hex(s)
print(h)
s = binascii.a2b_hex(h)
print(s)

# 只能大写
import base64
h = base64.b16encode(s)
print(h)
s = base64.b16decode(h)
print(s)

# Some byte data
s = b'hello'
import base64
# Encode as Base64
a = base64.b64encode(s)
print(a)
# Decode from Base64
print(base64.b64decode(a))

print('=' * 20)

from struct import Struct


def write_records(records, format, f):
    '''
    Write a sequence of tuples to a binary file of structures.
    '''
    record_struct = Struct(format)
    for r in records:
        f.write(record_struct.pack(*r))


# Example
records = [(1, 2.3, 4.5), (6, 7.8, 9.0), (12, 13.4, 56.7)]
with open('./tmp/data.b', 'wb') as f:
    write_records(records, '<idd', f)


def read_records(format, f):
    record_struct = Struct(format)
    chunks = iter(lambda: f.read(record_struct.size), b'')
    return (record_struct.unpack(chunk) for chunk in chunks)


# Example
if __name__ == '__main__':
    with open('./tmp/data.b', 'rb') as f:
        tmp = list(rec for rec in read_records('<idd', f))
        print(tmp)


def unpack_records(format, data):
    record_struct = Struct(format)
    return (record_struct.unpack_from(data, offset)
            for offset in range(0, len(data), record_struct.size))


# Example
if __name__ == '__main__':
    with open('./tmp/data.b', 'rb') as f:
        data = f.read()
    tmp = list(rec for rec in unpack_records('<idd', data))
    print(tmp)

from struct import Struct
record_struct = Struct('<idd')
print(record_struct.size)
_ = record_struct.pack(1, 2.0, 3.0)
print(_)
print(record_struct.unpack(_))

print('=' * 20)

