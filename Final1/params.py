'''
坑：如果你的默认值参数是一个可变的数据类型，则该参数会被共享
后果：破坏了函数的幂等性
'''
def func(val, lst=[]):
    lst.append(val)
    print(lst)


'''
使之重新满足幂等性的方法: 形参个数与实参保持一致
'''
def function(val):
    lst = []
    lst.append(val)
    print(lst)


'''
动态传参
'''
def shi(*food):
    print(food)


def jia(**food):
    print(food)


if __name__ == '__main__':
    func(1)
    func(1)
    print('========================================')
    function(1)
    function(2)
    print('========================================')
    shi('rice')
    shi('rice', 'noodles')
    print('========================================')
    jia(entree='dumplings', main='ramen')