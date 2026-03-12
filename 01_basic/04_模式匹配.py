# 模式匹配
space = 5

match space:
    case 1:
        print('1个空格')
    case 2:
        print('2个空格')
    case 3:
        print('3个空格')
    case _:  # 表示匹配到其他任何情况
        print('其他空格')   


'''match可以匹配多个值'''
space = 5

match space:
    case x if x < 10: # 匹配小于10的空格
        print(f'< 10 spaces: {x}')
    case 10:
        print('10 spaces.')
    case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
        print('11~18 spaces.')
    case 19:
        print('19 spaces.')
    case _:
        print('其他空格')   

# match可以匹配列表
space = [1, 2, 3, 4, 5]

match space:
    case [1, 2, 3, 4, 5]:
        print('12345 spaces.')
    case _:
        print('匹配列表')   
