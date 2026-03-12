# try except 错误处理

try:
  r = 10 / 0
except ZeroDivisionError as e:
  print("除数不能为0")
finally:
  print("finally")

# 捕获错误可跃迁层级
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')

main()


# 记录错误日志
import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')



