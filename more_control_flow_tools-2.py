# 声明一个函数
def fib(i):
    """ print a fibonacci series up to n"""
    a,b = 0,1
    while a < i:
        print(a, end= ' ')
        a,b = b,a+b
    print()

fib(2000)


# More on Define Functions
# Default Arguments Values
def ask_ok(prompt, retries=4, reminder="Please Try Again"):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError("invalid user input")
        print(reminder)
# ask_ok("y")
# ask_ok("ye")
# ask_ok("yes")
# ask_ok(1212)


# The default values are evaluated at the point of function definition in the defining scope
# The default value is evaluated only once
i = 5
def f(arg=i):
    print(arg)

i = 6
f() # print 5


# 数组[Array、Object这样写会改变]
def fa(a, L=[]):
    L.append(a)
    return L
print(fa(1))
print(fa(2))
print(fa(3))

# 数组,这样不改变
def faNoChange(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
print(faNoChange(4))
print(faNoChange(5))
print(faNoChange(6))


# Keyword Arguments
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print('-- This parrot would not', action, end= ' ')
    print(' if you put', voltage, 'volts through it.')
    print('-- Lovely plumage, the', type)
    print('-- It is', state, '!')

# parrot(1000)
# parrot(voltage=1000)
# parrot(voltage=1000, action='VOOOOOM')
# parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
# parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

#** name 映射类型,字典类型
def cheeseshop(kind, *arguments, **keywords):
    print('-- Do you have any', kind, '?')
    print('-- I am sorry,  we are all out of', kind)
    for arg in arguments:
        print(arg)
    print('-' * 40)
    for kw in keywords:
        print(kw, keywords[kw])

cheeseshop('瘦瘦','美丽', '大方', '可爱', '富有魅力', '蠢萌', old='18',weight='100')


# 函数注释
def f(ham: str, eggs: str = 'eggs') -> str:
    print('Annotions', f.__annotations__)
    print('Arguments', ham, eggs)
    return ham + ' and ' + eggs

f('spam')