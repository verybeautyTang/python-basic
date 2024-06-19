"""
华氏温度转换为摄氏温度
提示：华氏温度到摄氏温度的转换公式为：C = (F - 32) / 1.8。
"""

f = float(input('当前华氏温度是:'))
c = (f - 32) / 18
print('%.1f华氏度 = %.1f摄氏度度' % (f, c))


"""
输入圆的半径计算计算周长和面积
"""

radius = float(input('请输入圆的面积: '))
perimeter =2 * 3.14 * radius
area = 3.14 * radius * radius
print('周长: %.2f' % perimeter)
print('面积: %.2f' % area)


"""
输入年份判断是不是闰年
"""

year = int(input('请输入年份: '))
is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(is_leap)