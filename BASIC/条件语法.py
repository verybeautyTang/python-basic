"""
用户身份认证
"""
username = input('请输入用户名: ')
password = input('请输入口令: ')
if username == 'admin' and password == '123456':
    print('身份验证成功')
else:
    print('身份验证失败')


"""
分段函数求值
"""

x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print(f'f({x}) = {y}')

# 英制单位英寸与公制单位厘米互换。
value = float(input('请输入长度: '))
unit = input('请输入单位: ')
if unit == 'in' or unit == '英寸':
    print('%f英寸 = %f厘米' % (value, value * 2.54))
elif unit == 'cm' or unit == '厘米':
    print('%f厘米 = %f英寸' % (value, value / 2.54))
else:
    print('请输入有效的单位')

# 百分制成绩转换为等级制成绩

score = float(input('请输入成绩: '))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print('对应的等级是:', grade)

# 输入三条边长，如果能构成三角形就计算周长和面积。

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
    peri = a + b + c
    print(f'周长: {peri}')
    half = peri / 2
    area = (half * (half - a) * (half - b) * (half - c)) ** 0.5
    print(f'面积: {area}')
else:
    print('不能构成三角形')