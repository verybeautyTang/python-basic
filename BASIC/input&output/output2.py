# 手动格式化string
for x in range(1, 11):
    print(repr(x).rjust(2),repr(x * x).rjust(1),end= ' ')
    print(repr(x*x*x).rjust(4))
 # 1   1    1
 # 2   4    8
 # 3   9   27
 # 4  16   64
 # 5  25  125
 # 6  36  216
 # 7  49  343
 # 8  64  512
 # 9  81  729
 # 10 100 1000

# 字符串对象的 str.rjust() 方法通过在左侧填充空格来右对齐给定宽度字段中的字符串
# 还有类似的方法 str.ljust() 和 str.center() 。


# 还有另一种方法 str.zfill() ，它用零填充左侧的数字字符串。它理解加号和减号：
print('12'.zfill(5))  # 00012

print('-3.14'.zfill(7))  # -003.14

print('3.14159265359'.zfill(5))  # 3.14159265359



# old string format

import math
print('The value of pi is approximately %5.3f' % math.pi)  # The value of pi is approximately 3.142


# 读写文件
# reading and writing files


# open(文件的字符串名称, 描述文件的使用方式, 文件的文本模式)
# 描述文件的使用方式
    # w: 仅仅写入
    # a: 追加的文件
    # r: 仅被读取[默认]
    # r+:可以进行读写
# 文本的文本模

# files = open('workfile', 'w', encoding='utf-8')


# 正常处理文件对象时候,最好使用with关键字,优点是在文件完成后会关闭,即使发生了异常也是这样.
with open('workfile', 'r', encoding='utf-8') as f:
    read_data = f.read()
    # print(read_data)

print(f.closed)  # True

# 如果不使用with关键字,那么应该调用f.close()关闭文件并且理解释放他使用的任何资源


# File Object的方法
with open('workfile', 'r', encoding='utf-8') as f:

    # 这是阅读文件的方法.整个文件
    # print(f.read())

    # 这是阅读文件每一排的方法
    print(f.readline())
    # print(f.readline())
    # print(f.readline())

    # 这是添加文件
    # f.write('你好,我刚刚添加了一个数据,我不知道对不对')

    # 除了string类型的自动被添加上去之后,其他的都会自动转换成string类型
    value = ('the answer', 42)
    s = str(value)   # convert the tuple to string
    # f.write(s)

    # 返回一个整数,给出文件对象在文件中的当前位置,在二进制模式下表示为从头开始的字节数,在文本模式下表示为不透明数字
    # print(f.tell(10))

    # 要更改文件对象的位置，请使用 f.seek(offset, whence)
    print(f.seek(5))

import json
x = [1, 'simple', 'list']
y = json.dump(x, f)
print(y)
