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

