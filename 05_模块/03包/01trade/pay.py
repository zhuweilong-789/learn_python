
def wechant_pay(amount):
    print(f"微信支付{amount}元")
def ali_pay(amount):
    print(f"支付宝支付{amount}元")
def info():
    print("这是一个支付模块")

# 通过 __all__ 变量指定from pay import * 引入的函数
__all__ = ["wechant_pay", "ali_pay"]
__name__ #是动态的，当模块被直接运行时，__name__ 为 "__main__"，当模块被引入时，__name__ 为模块名
