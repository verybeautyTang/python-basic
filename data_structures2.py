# 元组和序列
# 元素由多个逗号分隔的值组成
tuples = 12345,  54321, 'hello!'
print(tuples[0]) # 12345

print(tuples) # (12345, 54321, 'hello!')

tuples_nestes = tuples, (1, 2, 3, 4, 5)
print(tuples_nestes) #((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))


# 'tuple' object does not support item assignment
#  元组是不可变的,但是列表是可以变的
# tuples[0] = 8888
# print(tuples)  # 这里会报错


empty = ()
singleton = 'hello', # 这是元组
singleton1 = 'hello'

print(len(empty) ) # 0
print(len(singleton)) # 1
print(len(singleton1)) # 5

print(singleton)


#set 集合,无重复元素的无序集合,基本用于测试和消除重复的条目,这里支持数学运算, 例如并集、交集、和对称差值

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

print('orange' in basket) # True

print('water melon' in basket) # False

# Demonstrate set operations on unique letters from two words
a = set('abidjkhsdach')
b = set('sdjhzmadk')

print(a)  # {'c', 'a', 'k', 'h', 'b', 's', 'j', 'i', 'd'}

print(a - b)  # {'c', 'b', 'i'} a有的b没有的

print(a | b)  # {'s', 'j', 'h', 'm', 'i', 'k', 'z', 'd', 'c', 'b', 'a'} a 和b都有的

print(a ^ b)  # {'b', 'z', 'c', 'm', 'i'}  letters in a or b but not both

print(a & b)  # {'d', 'j', 'k', 'h', 's', 'a'} a和b都有的


# 字典 Dictionaries
# 使用索引、键可以是任何不可变类型, 字符串和数字都可以作为键
tel = {
 'jack': 4098,
 'sape': 4139
}
tel['guido'] = 4127

print(tel)  # {'jack': 4098, 'sape': 4139, 'guido': 4127}

print(tel['jack'])  # 4098

del tel['guido']

print(tel)  # {'jack': 4098, 'sape': 4139}

tel['irv'] = 4127

print(tel)  # {'jack': 4098, 'sape': 4139, 'irv': 4127}

print(list(tel))  # ['jack', 'sape', 'irv']

print(sorted(tel))  # ['irv', 'jack', 'sape']

print('jack' in tel)  # True

print('hello' not in tel)  # True


# dict() 构造函数可以从键值对序列构建字典
dict1 = dict([('one', 1), ('two', 2), ('three', 3)])
print(dict1)  # {'one': 1, 'two': 2, 'three': 3}

# 当键是简单字符串时，有时使用关键字参数指定对会更容易
dict2 = dict(one=1, two=2, three=3)
print(dict2)  # {'one': 1, 'two': 2, 'three': 3}


# 字典推导式可用于从任意键和值表达式创建字典
dict3 = {x: x**2 for x in (2, 4, 6)}

print(dict3)  # {2: 4, 4: 16, 6: 36}


# 循环

# 1、 循环字典时，可以使用 items() 方法同时检索键和对应的值。
knignt = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knignt.items():
    print(k, v)

# 2、循环序列时，可以使用 enumerate() 函数同时检索位置索引和相应的值。
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# 3、要同时循环两个或多个序列，可以将条目与 zip() 函数配对。
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))


# 反向循环列表
for i in reversed(range(1, 10, 4,)):
    print(i)

# 要按排序顺序循环序列，请使用 sorted() 函数，该函数返回新的排序列表，同时保持源不变;
basket13 = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket13):
    print(i)

# 在序列上使用 set() 可以消除重复元素。在序列上结合使用 sorted() 和 set() 是按排序顺序循环序列中唯一元素的惯用方法。
for f in sorted(set(basket13)):
    print(f)