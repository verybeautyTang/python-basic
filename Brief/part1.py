# Brief Tour of the Standard Library

#  Operating System Interface

import os
#  # Return the current working directory
print(os.getcwd()) # /Users/happyelements/study/python-basic/Brief

# # Change current working directory
# print(os.chdir('/classes/'))

# Run the command mkdir in the system shell
print(os.system('mkdir today')) # 256 mkdir: today: File exists

# 请务必使用 import os 样式而不是 from os import * 。这将防止 os.open() 隐藏内置 open() 函数，该函数的操作方式有很大不同

# 内置的 dir() 和 help() 函数可用作交互辅助工具，用于处理 os 等大型模块

# print(dir(os))
#
# print(help(os))

# 对于日常文件和目录管理任务， shutil 模块提供了更易于使用的更高级别的接口：

import  shutil

# copy 复制命令
# print(shutil.copy('data.db','archive.db'))

# move 移动命令
# print(shutil.move('/build/executables', 'installdir'))


# 文件通配符
# glob 模块提供了从目录通配符搜索中创建文件列表的功能

import glob
# 查找当前文件的文件列表
print(glob.glob('*.py'))


# 命令行参数
import sys
print(sys.argv)
# argparse 模块提供了更复杂的机制来处理命令行参数。以下脚本提取一个或多个文件名以及要显示的可选行数
# import  argparse
# parser = argparse.ArgumentParser(
#     prog='top',
#     description='show top lines from each file')
# parser.add_argument('filenames', nargs='+')
# parser.add_argument('-l', '--lines', type=int, default=10)
# args=parser.parse_args()
# 错误输出重定向和程序终止
sys.stderr.write('Waring, log file not found starting a new one\n')


# 字符串模式匹配
# re 模块提供了用于高级字符串处理的正则表达式工具。对于复杂的匹配和操作，正则表达式提供了简洁、优化的解决方案
import re
findall1 = re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
print(findall1)  # ['foot', 'fell', 'fastest']

sub1 = re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
print(sub1)  # cat in the hat

# 当只需要简单的功能时，首选字符串方法，因为它们更易于阅读和调试
print('tea for too'.replace('too', 'two'))  # tea for two


# 数学
import  math
print(math.cos(math.pi / 4))  # 0.7071067811865476
print(math.log(1024, 2))  # 10.0
# random函数提供了进行随机选择的工具
import random
random1 = random.choice(['apple', 'pear', 'banana'])
print(random1)

random2 = random.sample(range(100), 10)
print(random2)

random3 = random.random()
print(random3)

random4 = random.randrange(6)
print(random4)
# statistics 模块计算数值数据的基本统计属性（平均值、中位数、方差等）
import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print(statistics.mean(data))
print(statistics.median(data))
print(statistics.variance(data))




