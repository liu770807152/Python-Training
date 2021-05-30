'''
函数的参数传递到底是传值，还是传引用？
'''
def weird_func_1(param: str):
    param = param + '.'
    param = param.replace('i', 'I', 1)
    return param


def weird_func_2(param: list):
    param.append(0)
    return param

'''
函数没有return语句，就真的没有返回值吗？
'''
def no_return_func(first = 0, second = 0):
    sum = first + second

if __name__ == '__main__':
    s = 'i am a string'
    l = [3, 2, 1]
    print('Return result: ' + weird_func_1(s))
    print('After execution: ' + s)
    print('Return result: ' + str(weird_func_2(l)))
    print('After execution: ' + str(l))
    print('The return value of no_return_func is: ' + str(no_return_func(1, 2)))