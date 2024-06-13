year = 2024
event = "Referendum"
print(f'Result of the {year} {event}')  # Result of the {year} {event}


# src.format,手动工作,需要使用{}来标记变量和被提海岸的位置,并可以提供详细的格式化指令
yes_vote = 42_572_654
no_votes = 43_132_495
percentage = yes_vote / (yes_vote + no_votes)
print('{:-9} YES votes {:2.2%}'.format(yes_vote, percentage))

# 使用repr()、str()函数将任何数据

s = 'Hello, world'
print(str(s))  # Hello, world
print(repr(s))  #'Hello, world'

print(str(1 / 7))

x = 10 * 3.25
y = 200 * 200

z = 'The value of x is ' + repr(x) + ', and y is' + repr(y) + '...'
print(z)

hello = 'hello world \n'
hellos = repr(hello)
print(hellos)

print(repr((x, y, ('spam','eggs'))))


# Formatted String Literals
# 格式化字符串文字（也简称为 f 字符串）允许您通过在字符串中添加 f 或 F 前缀并将表达式编写为{expression}
# 在 ':' 之后传递一个整数将导致该字段的字符宽度达到最小数量。这对于使列对齐非常有用。
import math
print(f'The value of pi is a approximately {math.pi:.3f}')  # The value of pi is a approximately 3.142

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')
    # Sjoerd     ==>       4127
    # Jack       ==>       4098
    # Dcab       ==>       7678


# 可以使用其他修饰符在格式化值之前对其进行转换。 '!a' 应用 ascii() ， '!s' 应用 str() ， '!r' 应用 repr() ：
animals ='eels'
print(f'My hovercraft is {animals}')  # My hovercraft is eels
print(f'My hovercraft is {animals!r}')  # My hovercraft is 'eels'

# 字符串format()方法
# 其中的括号和字符（称为格式字段）将替换为传递到 str.format() 方法中的对象。括号中的数字可用于引用传递到 str.format() 方法中的对象的位置。
print('We are the {} who say "{}!"'.format('knights', 'Ni'))  # We are the knights who say "Ni!"

print('{0} and {1}'.format('spam', 'eggs'))  # spam and eggs

print('{1} and {0}'.format('spam', 'eggs'))  # eggs and spam


#  str.format() 方法中使用关键字参数，则通过使用参数名称来引用它们的值。
print('This {food} is {adjective}.'.format(
    food='spam',
    adjective='absolutely horrible'
))  # This spam is absolutely horrible.

# 位置参数和关键字参数可以任意组合：
print('The story of {0},{1}, and {other}.'.format('Bill','Manfred', other='Georg'))  # The story of Bill,Manfred, and Georg.

# 如果不想拆分,可以按照'[]'来访问键来完成
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
print('Jack:{0[Jack]:d}; Sjoerd: {0[Sjoerd]:d};Dcab: {0[Dcab]:d}'.format(table))  # Jack:4098; Sjoerd: 4127;Dcab: 7678


# 这也可以通过使用“**”符号将表作为关键字参数传递来完成。
print('Jack:{Jack:d}; Sjoerd: {Sjoerd:d};Dcab: {Dcab:d}'.format(**table))  # Jack:4098; Sjoerd: 4127;Dcab: 7678

# 这与内置函数 vars() 结合使用特别有用，该函数返回包含所有局部变量的字典。
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
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

