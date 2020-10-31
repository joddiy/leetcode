# 读写文本数据
# Read the entire file as a single string
# with open('somefile.txt', 'rt') as f:
#     data = f.read()
#     print(data)
# print('=' * 20)

# # Iterate over the lines of the file
# with open('somefile.txt', 'rt') as f:
#     for line in f:
#         print(line)
# print('=' * 20)

# # Write chunks of text data
# with open('somefile.txt', 'wt') as f:
#     f.write(text1)
#     f.write(text2)
# print('=' * 20)

# # Redirected print statement
# with open('somefile.txt', 'wt') as f:
#     print(line1, file=f)
#     print(line2, file=f)
#     ...

# 读写字节数据
# # Read the entire file as a single byte string
# with open('somefile.bin', 'rb') as f:
#     data = f.read()

# # Write binary data to a file
# with open('somefile.bin', 'wb') as f:
#     f.write(b'Hello World')

# 二进制I/O还有一个鲜为人知的特性就是数组和C结
# 构体类型能直接被写入，而不需要中间转换为自己对象。比如：
import array
nums = array.array('i', [1, 2, 3, 4])
with open('./tmp/data.bin', 'wb') as f:
    f.write(nums)

a = array.array('i', [0, 0, 0, 0, 0, 0, 0, 0])
with open('./tmp/data.bin', 'rb') as f:
    f.readinto(a)
print(a)

# 文件不存在才能写入
# with open('./tmp/somefile', 'xt') as f:
#     f.write('Hello\n')

print('=' * 20)

import io
s = io.StringIO()
s.write('Hello World\n')
print('This is a test', file=s)
print(s.getvalue())
s = io.StringIO('Hello\nWorld\n')
print(s.read(4))
print(s.read())
print('-' * 20)

s = io.BytesIO()
s.write(b'binary data')
print(s.getvalue())
# 需要注意的是， StringIO 和 BytesIO 实例并没有正确的整数类型的文件描述符
print('=' * 20)

text = 'Hello World\n'

# gzip compression
import gzip
with gzip.open('./tmp/somefile.gz', 'wt') as f:
    f.write(text)

# bz2 compression
import bz2
with bz2.open('./tmp/somefile.bz2', 'wt') as f:
    f.write(text)

# gzip compression
import gzip
with gzip.open('./tmp/somefile.gz', 'rt') as f:
    text = f.read()

# bz2 compression
import bz2
with bz2.open('./tmp/somefile.bz2', 'rt') as f:
    text = f.read()

# encoding，errors，newline
with gzip.open('somefile.gz', 'wt', compresslevel=5) as f:
    f.write(text)

import gzip
f = open('somefile.gz', 'rb')
with gzip.open(f, 'rt') as g:
    text = g.read()

print('=' * 20)

# 固定大小记录的文件迭代
# from functools import partial

# RECORD_SIZE = 32

# with open('somefile.data', 'rb') as f:
#     records = iter(partial(f.read, RECORD_SIZE), b'')
#     for r in records:
#         pass

import os.path


# 文件对象的 readinto() 方法能被用来为预先分配内存的数组填充数据
def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        f.readinto(buf)
    return buf


# Write a sample file
with open('./tmp/sample.bin', 'wb') as f:
    f.write(b'Hello World')

buf = read_into_buffer('./tmp/sample.bin')
print(buf)
buf[0:5] = b'Hello'
print(buf)
with open('./tmp/newsample.bin', 'wb') as f:
    f.write(buf)

# 零复制
m1 = memoryview(buf)
m2 = m1[-5:]
print(m2)
m2[:] = b'WORLD'
print(buf)

print('=' * 20)

import os
import mmap


def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)


# 内存映射的二进制文件
size = 1000000
with open('./tmp/data', 'wb') as f:
    f.seek(size - 1)
    f.write(b'\x00')

with memory_map('./tmp/data') as m:
    print(len(m))
    print(m[0:10])
    # Reassign a slice
    m[0:11] = b'Hello World'

# Verify that changes were made
with open('./tmp/data', 'rb') as f:
    print(f.read(11))

m = memory_map('./tmp/data')
# Memoryview of unsigned integers
v = memoryview(m).cast('I')
v[0] = 7
print(m[0:4])
m[0:4] = b'\x07\x01\x00\x00'
print(v[0])

print('=' * 20)

import os
path = './tmp/data'
# Get the last component of the path
print(os.path.basename(path))
# Get the directory name
print(os.path.dirname(path))
# Join path components together
print(os.path.join('tmp', 'data', os.path.basename(path)))
# Expand the user's home directory
path = './tmp/data'
print(os.path.expanduser(path))
# Split the file extension
print(os.path.splitext(path))

print('=' * 20)

print(os.path.exists('/etc/passwd'))
print(os.path.isfile('/etc/passwd'))
print(os.path.isdir('/etc/passwd'))
print(os.path.islink('/usr/local/bin/python3'))
print(os.path.realpath('/usr/local/bin/python3'))
import time

print(os.path.getsize('/etc/passwd'))
print(os.path.getmtime('/etc/passwd'))
print(time.ctime(os.path.getmtime('/etc/passwd')))

print('=' * 20)

#
import os
names = os.listdir('/tmp')
print(names)

# Get all regular files
names = [
    name for name in os.listdir('/tmp')
    if os.path.isfile(os.path.join('/tmp', name))
]
print(names)

# Get all dirs
dirnames = [
    name for name in os.listdir('/tmp')
    if os.path.isdir(os.path.join('/tmp', name))
]
print(dirnames)

# 对于文件名的匹配，你可能会考虑使用 glob 或 fnmatch 模块
import glob
pyfiles = glob.glob('./tmp/*.bin')
print(pyfiles)

from fnmatch import fnmatch
pyfiles = [name for name in os.listdir('./tmp') if fnmatch(name, '*.bin')]
print(pyfiles)

print('=' * 20)


# 打印不合法的文件名
def bad_filename(filename):
    return repr(filename)[1:-1]


# try:
#     print(filename)
# except UnicodeEncodeError:
#     print(bad_filename(filename))

import sys
print(sys.stdout.encoding)
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='latin-1')
print(sys.stdout.encoding)
sys.stdout.flush()

sys.stdout.buffer.write(b'Hello\n')
print('=' * 20)

# 将文件描述符包装成文件对象
# Open a low-level file descriptor
import os
fd = os.open('./tmp/somefile.txt', os.O_WRONLY | os.O_CREAT)

# Turn into a proper file
f = open(fd, 'wt')
f.write('hello world\n')
f.close()

# Create a file object, but don't close underlying fd when done
# f = open(fd, 'wt', closefd=False)

# Create a binary-mode file for stdout
sys.stdout.flush()
bstdout = open(sys.stdout.fileno(), 'wb', closefd=False)
bstdout.write(b'Hello World\n')
bstdout.flush()
print('=' * 20)

from tempfile import TemporaryFile

with TemporaryFile('w+t') as f:
    # Read/write to the file
    f.write('Hello World\n')
    f.write('Testing\n')

    # Seek back to beginning and read the data
    f.seek(0)
    data = f.read()
    print(data)
# Temporary file is destroyed

from tempfile import NamedTemporaryFile

with NamedTemporaryFile('w+t') as f:
    print('filename is:', f.name)
# File automatically destroyed

with NamedTemporaryFile('w+t', delete=False) as f:
    print('filename is:', f.name)

from tempfile import TemporaryDirectory

with TemporaryDirectory() as dirname:
    print('dirname is:', dirname)
    # Use the directory
# Directory and all contents destroyed
f = NamedTemporaryFile(prefix='mytemp', suffix='.txt', dir='/tmp')
print(f.name)

print('=' * 20)

import pickle
data = [1, 2, 3]
f = open('./tmp/somefile', 'wb')
pickle.dump(data, f)
f.close()

# Restore from a file
f = open('./tmp/somefile', 'rb')
data = pickle.load(f)
f.close()

print(data)

# countdown.py
import time
import threading


class Countdown:
    def __init__(self, n):
        self.n = n
        self.thr = threading.Thread(target=self.run)
        self.thr.daemon = True
        self.thr.start()

    def run(self):
        while self.n > 0:
            print('T-minus', self.n)
            self.n -= 1
            time.sleep(5)

    def __getstate__(self):
        return self.n

    def __setstate__(self, n):
        self.__init__(n)


c = Countdown(30)

# After a few moments
f = open('cstate.p', 'wb')
import pickle
pickle.dump(c, f)
f.close()

# 从序列化的地方恢复过来
f = open('cstate.p', 'rb')
pickle.load(f)
