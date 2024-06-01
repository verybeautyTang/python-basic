# https://docs.python.org/3/tutorial/controlflow.html
# if语句[ if elif else ]
x = int(input('Please enter an integer: ' ))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')


# for语句
# 直接输出数据
words = ['cat', 'window', 'defenestrate']
for w  in words:
    print(w, len(w))

# 集合、对象 用for拿到数据
# key: status的形式
users = {
    'Hans': 'active',
    'English': 'inactive',
    'Japan': 'active'
}

for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
active_user = {}
for user, status in users.copy().items():
    if status == 'active':
        active_user[user] = status
        print(user, status)
        print(active_user)


# range函数
# 只有1个参数的情况下,从0开始,数n个数
# 有2个参数的情况下,则第一个参数为起始参数,第二个参数为最后一个参数 [n,m)且不能超过最大参数
# 如有3个参数的情况下, 第一个参数为起始参数,第三个参数为每次需要增加的数据, 第二个参数为最大的参数且不能超过最大参数
for i in range(5):
    print(i) # 0 1 2 3 4

range1 = list(range(5, 10))
print(range1) # 5,6,7,8,9

range2 = list(range(0, 10, 3))
print(range2) # 0 3 6 9

range3 = list(range(-10, -100, -30))
print(range3) # -10 -40 -70

# 根据数组里面可以给range函数传递数据
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

# range可以根math函数一起用
sum1 = sum(range(4))
print(sum1) # 0 + 1+ 2 + 3  = 6


# break and continue函数

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
        else:
            print(n, 'is a prime number')