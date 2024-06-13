# 引入模块 方法1
# Python解释器并使用以下命令导入该模块, 直接倒入
import modules

modules.fib(1000)

print(modules.__name__)

# 引入模块 方法二
# 防止所有函数用作全局符号表,所以这里可以将模块的名称放在导入模块的全局符号表中
from modules import fib, fib1
fib(1000)
fib1(1000)

# 引入模块 方法三
# 甚至还有一个变体可以导入模块定义的所有名称：
from modules import  *
fib(1000)


# 引入模块 方法四
# 如果模块名称后跟 as ，则 as 后面的名称将直接绑定到导入的模块
import modules as fib
fib.fib(1000)


# 引入模块 方法五
# 它也可以在使用 from 时使用，具有类似的效果：

from modules import fib as fibonacci

fibonacci(1000)