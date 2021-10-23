'''
分清全局变量和局部变量，而且不要使用全局变量
'''
i = 0
def a():
    i = 1
    print('local:', i)
a()
print('global:', i)

'''
有没有办法在函数中使用全局变量？有！
1. 不要对全局变量进行赋值，就可以使用同名的全局变量
2. 使用global关键字(应该不考)
3. 使用nonlocal关键字(应该不考)
'''
i = 0
def a():
    global i
    i = 1
    print('local:', i)
a()
print('global:', i)

'''
例题

def func(a):
    if b < 0:
        a = 1
    b = 0
    return a
func(i)
'''