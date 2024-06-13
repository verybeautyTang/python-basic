# while True print('Hello world')
# Handling Exceptions
# 可以编写处理选定异常的程序。看下面的示例，它要求用户输入，直到输入有效的整数为止，但允许用户中断程序（使用 Control-C 或操作系统支持的任何内容）
# ；请注意，用户生成的中断是通过引发 KeyboardInterrupt 异常来发出信号的。
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")



# expect
# Exception 可以用作捕获（几乎）所有内容的通配符。然而，最好的做法是尽可能具体地说明我们打算处理的异常类型，并允许任何意外的异常继续传播。
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(inst)
    print(type(inst))
    print(inst.args)

    x,y = inst.args
    print('x = ', x)
    print('y = ', y)

# 引发异常
# raise语句允许程序员强制发生指定的异常
# raise NameError('HiThere')  # NameError: HiThere


# 如果需要确定是否引发异常但不打算处理它，则可以使用更简单的 raise 语句形式重新引发异常
# try:
#     raise Exception('HiThat')
# except NameError:
#     print('An exception was raised')
#     raise





# 异常链接 Exception Chaining
# 如果except部分内未处理的异常,则会将正在处理的异常附加到该部分并包括在错误信息中
try:
    open('database.sqlite')
except OSError:
    raise  RuntimeError('unable to open file')