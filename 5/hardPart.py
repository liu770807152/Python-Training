'''
对于基础数据类型，如数字、字符串，在参数传递时，只拷贝字面值
对于iterable对象，如list、set、dict，在参数传递时，只拷贝地址值
'''
def f(x):
    '''
    x是形参
    注意值拷贝和引用拷贝的区别！
    '''
    x += y
    return x

x = 1
y = 2
'''
x是实参
'''
z = f(x)
print(x, z, z == x)

print('=================================================')

def f1(ns):
    time = 5
    while time > 0:
        ns = ns + '1'
        time -= 1
    return ns


def f2(ns):
    time = 5
    while time > 0:
        ns.append(1)
        time -= 1
    return ns

a = '123'
aList = [1, 2, 3]
print(f1(a))  # 12311111
print(f2(aList))  # [1, 2, 3, 1, 1, 1, 1, 1]
print('函数执行后：')
print(a)  # 123
print(aList)  # [1, 2, 3, 1, 1, 1, 1, 1]