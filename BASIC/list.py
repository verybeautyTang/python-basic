# 在开始本节课的内容之前，我们先给大家一个编程任务，将一颗色子掷6000次，统计每个点数出现的次数。这个任务对大家来说应该是非常简单的，
# 我们可以用1到6均匀分布的随机数来模拟掷色子，然后用6个变量分别记录每个点数出现的次数，相信大家都能写出下面的代码。

import random
f1 = 0
f2 = 0
f3 = 0
f4 = 0
f5 = 0
f6 = 0
for _ in range(0, 6000):
    item= random.randint(1, 6)
    if item == 1:
        f1 += 1
    elif item == 2:
        f2 += 1
    elif item == 3:
        f3 += 1
    elif item == 4:
        f4 += 1
    elif item == 5:
        f5 += 1
    else:
        f6 += 1

print(f'1点出现了{f1}次')
print(f'2点出现了{f2}次')
print(f'3点出现了{f3}次')
print(f'4点出现了{f4}次')
print(f'5点出现了{f5}次')
print(f'6点出现了{f6}次')

# 上面的代码比较麻烦且不好用
# 在Python中,列表是有一系列元素按照特定顺序构成的数据结构,可以保存多个数据,且允许重复的数据

# 列表的运算符

items1 = [1, 23, 385, 23, 30, 434]
items2 = [45, 67, 89]

# 列表的拼接
items3 = items1 + items2
print(items3)

# 列表的重复
items4 = ['hello'] * 3
print(items4)

# 列表的成员运算
print(100 in items3)  # False
print('hello' in items4)  # True

# 获取列表的整个长度
size = len(items3)
print(size)

# 列表的索引
print(items3[0], items3[-size])
items3[-1] = 100
print(items3[size - 1], items3[-1])

# 列表的切片
print(items3[:5])
print(items3[4:])          # [55, 87, 45, 8, 100]
print(items3[-5:-7:-1])    # [55, 68]
print(items3[::-2])        # [100, 45, 55, 99, 35]


# 列表的比较运算
items5 = [1, 2, 3, 4]
items6 = list(range(1, 5))
# 两个列表比较相等性比的是对应索引位置上的元素是否相等
print(items5 == items6)    # True
items7 = [3, 2, 1]
# 两个列表比较大小比的是对应索引位置上的元素的大小
print(items5 <= items7)    # True



# 列表的遍历

itemsx =  ['Python', 'Java', 'Java', 'Go', 'Kotlin', 'Python']
for x in range(len(itemsx)):
    print(x)

for y  in itemsx:
    print(y)



# 列表的方法
# 添加和删除元素

# 使用append方法在列表尾部添加元素
itemsx.append('shoushou')
print(itemsx)

# 使用insert方法在列表指定索引位置插入元素
itemsx.insert(2, 'beautyTang')

# 删除指定的元素
itemsx.remove('Java')
print(itemsx)

# 元素位置和次数
# 查找元素的索引位置
print(itemsx.index('Python'))       # 0
print(itemsx.index('Python', 2))    # 5
# 注意：虽然列表中有'Java'，但是从索引为3这个位置开始后面是没有'Java'的
print(itemsx.index('Java', 3))      # ValueError: 'Java' is not in lis


# 元素排序和反转
# 排序
itemsx.sort()
print(itemsx)    # ['Go', 'Java', 'Kotlin', 'Python', 'Python']
# 反转
itemsx.reverse()
print(itemsx)    # ['Python', 'Python', 'Kotlin', 'Java', 'Go']


# 列表的生成式
# 创建一个由1到9的数字构成的列表
items1 = []
for x in range(1, 10):
    items1.append(x)
print(items1)

# 创建一个由'hello world'中除空格和元音字母外的字符构成的列表
items2 = []
for x in 'hello world':
    if x not in ' aeiou':
        items2.append(x)
print(items2)

# 创建一个由个两个字符串中字符的笛卡尔积构成的列表
items3 = []
for x in 'ABC':
    for y in '12':
        items3.append(x + y)
print(items3)


# 嵌套的列表
scores = [[0] * 3] * 5
print(scores)    # [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
