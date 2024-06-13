# 真 对(True) 假 错(False)
myNameIs = True

print(1 == 1)
print(1 == 2)
print(1 != 2)

# 0 标识空 表示没有
print(bool(1))
print(bool(0))

# '' 表示空 表示没有
print(bool(''))
print(bool('1111'))


# None 表示没有

print(bool(None))

# 如果x是False,那么表达式的结果就返回x,否则返回y
print(0 and 3)   # 0
# 如果x是False,那么表达式的结果就返回y,否则返回x
print(0 or 3)    # 3
# 如果x是False那么表达式的结果就是Ture,否则是False
print(not 3)    # False