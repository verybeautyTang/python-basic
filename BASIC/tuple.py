#元组也是多个元素按照一定的顺序构成的序列。
# 元组和列表的不同之处在于，元组是不可变类型，这就意味着元组类型的变量一旦定义，其中的元素不能再添加或删除，而且元素的值也不能进行修改。
# 定义元组通常使用()字面量语法，也建议大家使用这种方式来创建元组。元组类型支持的运算符跟列表是一样。

# 定义一个三元组
t1 = (30, 10, 55)

# 定义一个四元组
t2 = ('瘦瘦', 40, True, '阿美莉卡')

# 查看变量的类型
print(type(t1), type(t2))    # <class 'tuple'> <class 'tuple'>

# 查看元组中元素的数量
print(len(t1), len(t2))      # 3 4
# 通过索引运算获取元组中的元素

print(t1[0], t1[-3])         # 30 30
print(t2[3], t2[-1])         # 阿美莉卡 阿美莉卡


# 循环遍历元组中的元素
for member in t2:
    print(member)


# 成员运算
print(100 in t1)    # False
print(40 in t2)     # True

# 拼接
t3 = t1 + t2
print(t3)           # (30, 10, 55, '瘦瘦', 40, True, '阿美莉卡')


# 切片
print(t3[::3])      # (30, '瘦瘦', '阿美莉卡')

# 比较运算
print(t1 == t3)    # False
print(t1 >= t3)    # False
print(t1 < (30, 11, 55))    # True

# 一个元组中如果有两个元素，我们就称之为二元组；
# 一个元组中如果五个元素，我们就称之为五元组。
# 需要提醒大家注意的是，()表示空元组，但是如果元组中只有一个元素，需要加上一个逗号，
# 否则()就不是代表元组的字面量语法，而是改变运算优先级的圆括号，
# 所以('hello', )和(100, )才是一元组，而('hello')和(100)只是字符串和整数。

# 空元组
a = ()
print(type(a))    # <class 'tuple'>
# 不是元组
b = ('hello')
print(type(b))    # <class 'str'>
c = (100)
print(type(c))    # <class 'int'>
# 一元组
d = ('hello', )
print(type(d))    # <class 'tuple'>
e = (100, )
print(type(e))    # <class 'tuple'>


