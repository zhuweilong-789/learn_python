# try except 错误处理

try:
  r = 10 / 0
except ZeroDivisionError:
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

# BaseException 是所有错误的基类

