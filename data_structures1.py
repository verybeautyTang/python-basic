# list
# list.append(x)
# list.extend(x)
# list.insert(x)
# list.remove(x)
# list.pop([i])
# list.clear()
# list.index(x[,start[,end]])
# list.count(x)
# list.reverse()
# list.sort(*, key=None, reverse=False)
# list.copy()

#eg
fruits = ['apple', 'orange', 'pear', 'pineapple', 'banana']

print(fruits.count('apple') )# 1

print(fruits.index('banana')) #4

fruits.append('grape')
print(fruits)

fruits.sort()
print(fruits)

fruits.pop()
print(fruits)


# using lists as stacks
stack = [3, 4, 5]
stack.append(6)
stack.append(7)

print(stack)

stack.pop()
print(stack)

stack.pop()
stack.pop()
print(stack)


# using list as queues
from collections import  deque
queue = deque(['a', 'b', 'c'])
queue.append('d')
print(queue)

queue.popleft()
print(queue)


# list comprehensions
squares = []
for x in range(10):
    squares.append(x ** 2)
print(squares) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


equal_list = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]

print(equal_list) # [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

# equal_list与下面一致
equal_list1 = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            equal_list1.append((x, y))
print(equal_list1)


# if 和for的执行顺序是相同的,所以这里很多问题, 比如
vec = [-4, -2, 0 , 2, 4]
# create a new list with the values doubled
vec_list = [x ** 2 for x in vec]
print(vec_list) # [16, 4, 0, 4, 16]

# filter the list to exclude negative numbers
vec_list_filter = [x for x in vec if x >= 0]
print(vec_list_filter) # [0, 2, 4]

# apply a function to all the elements
vec_abs = [abs(x) for x in vec]
print(vec_abs) # [4, 2, 0, 2, 4]

# call a method on each element
freshfruit = [' banana', ' apple ', ' passion fruit         ']
freshfruit_list = [weapon.strip() for weapon in freshfruit]
print(freshfruit_list) #freshfruit

# create a list of 2-tuples like (number, square)
# 这里一点要打括号(x, x ** 2)
list_2_tuple = [(x, x ** 2) for x in range(6)]

print(list_2_tuple) #[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

# List comprehensions can contain complex expressions and nested functions:

from math import pi
pis = [str(round(pi, i) for i in range(1, 6))]
print(pis)


# 嵌套列表
matrix = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12] ]
rows = [[row[i] for row in matrix] for i in range(4)]
print(rows) # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# 与上面rows输出的一样
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed) # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# 这个也与上面一样
transposed1 = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed1.append(transposed_row)

print(transposed1)  # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]


# 实际上,内置了zip函数,
list_zip = list(zip(*matrix))
print(list_zip) #[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]


# del 语句 删除语句
# del与pop的区别是,del还可以用于清除整个列表、或者一个数据
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a) #[1, 66.25, 333, 333, 1234.5]

del(a[2: 4])
print(a) #[1, 66.25, 1234.5]

del a[:]
print(a)

# 删除变量,
del a
# print(a) #NameError: name 'a' is not defined



