'''
函数的参数传递到底是传值，还是传引用？
'''
def weird_func_1(param):
    param = param + '.'
    return param


def weird_func_2(param):
    param.append(0)
    return param

if __name__ == '__main__':
    s = 'I am a string'
    l = [3, 2, 1]
    print('Return result: ' + weird_func_1(s))
    print('After execution: ' + s)
    print('Return result: ' + weird_func_2(l))
    print('After execution: ' + l)