import math


def function_a():
    try:
        result = 1 / 0
    except ZeroDivisionError:  # except后面的异常类型要根据具体错误选择
        print("[function_a]除0异常")
    else:
        print("操作成功", "result=", result)


def function_b():
    try:
        result = math.a
    except AttributeError:
        print("[function_b]对象没有这个属性")
    else:
        print("操作成功", "result=", result)


def function_c():
    try:
        import lucky
    except ImportError:
        print("[function_c]导入模块/对象失败")
    else:
        print("操作成功", "result=", lucky)


if __name__ == '__main__':
    function_a()
    function_b()
    function_c()
