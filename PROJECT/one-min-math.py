# 一分钟数学运算

# 项目需求
# 直接在控制台使用命令行运行
# 程序运行之后倒计时1分钟之后结束
# 随机出100以内的2个整数加减乘除运算题目（除法确保能够除尽，但除数不能为0）
# 每出一道题目，由玩家给出答案，然后程序判断对错，接着出下一题，并且显示剩余时间
# 1分钟时间结束，显示总题数和正确率（正确率精确到小数点后2位），并将之前的题目和答案显示出来

# 项目练习
# 格式化字符串输出
# 循环
# 条件判断
# 列表
# 异常处理
# 自定义函数
# 时间工具包
# 随机工具包

import time
import random
def get_divisor(n):
    '''
     随机获得一个数n的整数除数。
    :param n: 一个整数
    :return: 一个数n的整数除数
    '''
    l =[]
    for i in range(1,n+1):
        if n % i == 0:
            l.append(i)
    return random.choice(l)

if __name__ == '__main__':
    ops = ['+', '-', '*', '/']
    start_time = time.time()
    total = 0
    current = 0
    questions = []
    while time.time() - start_time <= 60:
        a = random.randint(1, 99)
        op = random.choice(ops)
        if op == '/':
            # 如果是除法,b为a的一个随机整数
            b =get_divisor(a)
        else:
            b =random.randint(1, 99)
        # 正确答案
        a_op_b = '{}{}{}'.format(a, op, b)
        c = int(eval(a_op_b))

        # 让用户输入答案
        try:
            ans = int(input('{} ='.format(a_op_b)))
        except:
            ans =''
        # 检查是否正确
        if time.time() - start_time <= 60:
            if c == ans:
                print('正确! 剩余时间{}秒'.format(int(60 - (time.time() - start_time))))
                current = current + 1
            else:
                print('错误! 剩余时间{}秒'.format(int(60 - (time.time() - start_time))))
            total = total + 1
            questions.append('{} ={}'.format(a_op_b,ans))

    print('{}道题目, 正确率{:2f}$%'.format(total ,(current / total) * 100))

    for q in questions:
        print(q)