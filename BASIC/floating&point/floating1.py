from fractions import Fraction

x1 = 1 / 10
print(x1)


import math
# give 12 significant digits
print(format(math.pi, '.12g'))
# give 2 digits after the point
print(format(math.pi, '.2f'))


# 浮点数不相等
print(0.1 + 0.2 + 0.3 == 0.6)  # False

print(round(0.1, 1) + round(0.1, 1) + round(0.1, 1) == round(0.3, 1))  # False

# Though the numbers cannot be made closer to their intended exact values, the math.isclose() function can be useful
# for comparing inexact values
print(math.isclose(0.1 + 0.1 + 0.1, 0.3))  # True

print(round(math.pi, ndigits=2) == round(22 / 7, ndigits=2))  # True


# float.as_integer_ratio() 方法将浮点数的值表示为分数
# 这个比例是比较精确的,所以可以用来做计算
x = 3.14159
print(x.as_integer_ratio())  # (3537115888337719, 1125899906842624)

# 方法以十六进制（基数 16）表示浮点数 运用16进制表示浮点数
print(x.hex())

# sum函数也可以用于浮点数
print(sum([0.1] * 10) == 1.0)  # False
print(0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 == 1.0)  # False


# 精度丢失

arr = [-0.10430216751806065, -266310978.67179024, 143401161448607.16,
       -143401161400469.7, 266262841.31058735, -0.003244936839808227]
print(float(sum(map(Fraction, arr))))  # 8.042173697819788e-13

# math.fsum() 更进一步，在将值添加到运行总计中时跟踪所有“丢失的数字”，以便结果仅进行一次舍入。
print(math.fsum(arr))  # 8.042173697819788e-13

total = 0.0
for i in arr:
    total += i

print(total)  # -0.0051575902860057365

# 错误表示

