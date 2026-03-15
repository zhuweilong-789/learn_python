# 为什么需要处理异样：
# 1. 防止程序崩溃：当程序运行过程中发生错误时，如果不进行处理，程序会崩溃，导致用户体验下降
# 2. 提供错误信息：处理异常可以提供详细的错误信息，帮助开发人员定位和修复错误
# 3. 增强程序的健壮性：通过处理异常，程序可以在发生错误时继续运行，而不是立即终止

import traceback # 导入traceback模块，用于打印异常信息

try:
    a = int(input("请输入一个整数："))
    b = int(input("请输入另一个整数："))
    result = a / b
    print(result)
    print("x:", x)
except ValueError:
    print("请输入一个整数")
except ZeroDivisionError:
    print("除0错误")
# e是异常对象，包含了异常的详细信息
except Exception as e:
    print("未知错误", traceback.format_exc())
    print(e)  

