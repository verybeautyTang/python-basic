# 类继承机制允许多个基类,派生类可以覆盖其一个或者多个基类的任意方法,并且可以在一个方法啊里面调用同名基调的方法

# 范围和命名空间示例

#  global 赋值更改了整个模块内绑定
# nonlocal 赋值更改了函数内部绑定

def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
    def do_global():
        global spam
        spam = "global spam"
    spam = "test spam"

    do_local()
    print('After local assignment:', spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)



# basic class
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'Hello World'

x = MyClass()

print(x.i)
print(x.f())




# __init__创建 初始化空对象

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

y = Complex(1, 2)

print(y.r)
print(y.i)



# 实例对象
# 一般来说，实例变量用于每个实例唯一的数据，类变量用于类的所有实例共享的属性和方法：
class Dog:
    kind = 'canine'
    def __init__(self, name):
        self.name = name

d1 = Dog('John')
print(d1.kind)
print(d1.name)

d2 = Dog('Jack')
print(d2.kind)
print(d2.name)

# 正如关于名称和对象的一句话中所讨论的，共享数据对于涉及可变对象（例如列表和字典）可能会产生令人惊讶的效果。
# 例如，以下代码中的技巧列表不应用作类变量，因为所有 Dog 实例只会共享一个列表：

class Cat:
    tricks = [] # 这个Cat里面共享一个列表
    def __init__(self, name):
        self.name = name
    def add_trick(self, trick):
        self.tricks.append(trick)

c1 = Cat('John')
c1.add_trick('你好')
print(c1.name)
print(c1.tricks)  # ['你好']


c2 = Cat('Jack')
c2.add_trick('瘦瘦')
print(c2.name)
print(c2.tricks)  # ['你好', '瘦瘦']


# Random Remarks
# 如果相同的属性名称同时出现在实例和类中，则属性查找会优先考虑实例：
class Warehouse:
    purpose = 'storage'
    region = 'west'

w1 = Warehouse()
print(w1.purpose, w1.region)  # storage west

w2 = Warehouse()
w2.region = 'east'
print(w2.purpose, w2.region)  # storage east