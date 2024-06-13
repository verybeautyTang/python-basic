# 多线程
# 线程是一种用于解耦不顺序依赖的任务的技术。线程可用于提高在后台运行其他任务时接受用户输入的应用程序的响应能力。一个相关的用例是与另一个线程中的计算并行运行 I/O。
# 以下代码显示了高级 threading 模块如何在主程序继续运行的同时在后台运行任务：
# import threading, zipfile
#
# class AsyncZip(threading.Thread):
#     def __init__(self, infile, outfile):
#         threading.Thread.__init__(self)
#         self.infile = infile
#         self.outfile = outfile
#
#     def run(self):
#         f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
#         f.write(self.infile)
#         f.close()
#         print('Finished background zip of:', self.infile)
#
# background = AsyncZip('mydata.txt', 'myarchive.zip')
# background.start()
# print('The main program continues to run in foreground.')
#
# background.join()    # Wait for the background task to finish
# print('Main program waited until background was done.')

# logg打印
import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')


# Weak References 弱引用
import weakref, gc
class A:
    def __init__(self, x):
        self.x = x
    def __repr__(self):
        return str(self.x)

a = A(5)
d =weakref.WeakValueDictionary()
d['primary'] = a
print(d['primary'])  # 5

del a
print(gc.collect())  # 0

# print(d['primary'])  # 这个报错的额



# 处理列表的工具
# array 模块提供了一个 array() 对象，它就像一个列表，只存储同类数据，并且存储得更紧凑。以下示例显示了存储为两个字节无符号二进制数（类型代码 "H" ）
# 的数字数组，而不是 Python int 对象常规列表中每个条目通常的 16 个字节
from array import array
a = array('H',[4000, 10, 700, 22222])
print(sum(a))  # 26932

print(a[1: 3])  # array('H', [10, 700])

# collections 模块提供了一个 deque() 对象，它就像一个列表，从左侧追加和弹出速度更快，但在中间查找速度较慢。
# 这些对象非常适合实现队列和广度优先树搜索

from collections import deque
d = deque(["task1", "task2", "task3"])
d.append("task4")
print("Handling", d.popleft())   # Handling task1


#  十进制浮点运算
from decimal import *
round(Decimal('0.70') * Decimal('1.05'), 2)
# Decimal('0.74')
round(.70 * 1.05, 2)