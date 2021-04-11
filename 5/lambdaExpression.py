def func(num, n=2):
    return num ** n
print(func)

ret = func(10)
print(ret)

'''
匿名函数又被称为lambda表达式
语法: lambda 参数: 返回值
'''
fn = lambda num, n=2 : num ** n
print(fn)
ret = fn(10)
print(ret)