# 有许多用于访问互联网和处理互联网协议的模块。最简单的两个是用于从 URL 检索数据的 urllib.request 和用于发送邮件的 smtplib
from urllib.request import urlopen
with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
    for line in response:
        line = line.decode()
        if line.startswith('datetime'):
            print(line.rstrip())

# 本地主机上运行邮件服务器
# import smtplib
# server = smtplib.SMTP('localhost')
# server.sendmail('shiyu.he@happyelements.com',"""adsfkjh asjdflhasdfkljgasfhk""");


# 时间和日期
# datetime 模块提供了以简单和复杂方式操作日期和时间的类。虽然支持日期和时间算术，但实现的重点是有效的成员提取以进行输出格式化和操作。该模块还支持时区感知的对象。
from datetime import date
now = date.today()
print(now) # 2024-06-07

print(now.strftime('%m-%d-%y. %d %b %Y is a %A on the %d day of %B.')) # 06-07-24. 07 Jun 2024 is a Friday on the 07 day of June.

birthday = date(1998,9,17)
age = now - birthday
print(age.days)  # 9395


#  Data Compression 数据压缩
# 模块直接支持常见的数据归档和压缩格式，包括： zlib 、 gzip 、 bz2 、 lzma 、 zipfile 。
import zlib
s = b'which with has wrist watch bitch'
print(s)  # b'which with has wrist watch bitch'

t = zlib.compress(s)
print(t)  # b'x\x9c+\xcf\xc8L\xceP(\xcf,\xc9P\xc8H,V(/\xca,.Q(O,\x01\n&e\x02I\x00\xc6\xb0\x0c\x06'

print(zlib.decompress(t))  # b'which with has wrist watch bitch'

print(zlib.crc32(s))  # 1826538006


# 性能测量Performance Measurement
from timeit import Timer

# 使用元组打包和解包功能而不是传统的交换参数的方法可能很诱人。 timeit 模块很快就展现出了适度的性能优势
timer1 = Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
print(timer1) # 0.01137733299999999

timer2 = Timer('a,b = b,a', 'a=1; b=2').timeit()
print(timer2) # 0.010569332999999959


#  Quality Control 质量控制
def average(values):
    print(average([20, 30, 70]))
    """Compute the average of a list of numbers.
    >>> print(average([20,30,70]))
    40.0
    """
    return sum(values) / len(values)
import doctest
doctest.testmod()   # automatically validate the embedded tests


# unittest 模块不像 doctest 模块那样轻松，但它允许在单独的文件中维护更全面的测试集：

import unittest
class TestStatisticalFunctions(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average([20, 30, 70])

# Calling from the command line invokes all tests
unittest.main()


# Batteries include 包含电池
