# 循环结构

# 如果知道明确的循环执行的次数,推荐使用for-in做循环

"""
用for循环实现1-100的求和
"""
total =0
for x in range(0, 101):
    total += x
print(total)


"""
用for循环实现1~100之间的偶数求和
"""
total_odd = 0
for y in range(2, 101, 2):
    total_odd += y
print(total_odd)


# while循环,如果不知道具体的循环次数, 使用while进行循环

""" 
猜数字的游戏
计算机出一个1到100之间的随机数，
玩家输入自己猜的数字，计算机给出对应的提示信息（大一点、小一点或猜对了），如果玩家猜中了数字，计算机提示用户一共猜了多少次，游戏结束，否则游戏继续。
"""

"""
break关键字，它的作用是提前结束循环
continue，它可以用来放弃本次循环后续的代码直接让循环进入下一轮。
"""
import random
# 产生一个1-100范围的随机数
answer = random.randint(1,100)
counter =0
while(True):
    counter += 1
    numbers = int(input('请输入: '))
    if numbers < answer:
        print('大一点')
    elif numbers > answer:
        print('小一点')
    else:
        print('恭喜你,猜对了')
        break;

print(f'你一共猜测了{counter}次')


# 嵌套的循环结构

"""
打印99乘法表
"""
for i in range(1,10):
    for j in range(1, i +1):
        print(f'{i} * {j}={i * j}', end='\t')
    print()


"""
输入一个正整数判断它是不是素数。
"""
num = int(input('请输入一个正整数: '))
end = int(num ** 0.5)
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print(f'{num}是素数')
else:
    print(f'{num}不是素数')


"""
输入两个正整数计算它们的最大公约数和最小公倍数
"""
x = int(input('x = '))
y = int(input('y = '))
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print(f'{x}和{y}的最大公约数是{factor}')
        print(f'{x}和{y}的最小公倍数是{x * y // factor}')
        break