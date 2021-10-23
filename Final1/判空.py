# 一般我们用is来判空
c = None
if c is None:
    print("c是空")
else:
    print("c不是空")

'''
引申：
2015年真题：is和==的区别是什么? is比较引用的地址，==比较值大小
下面的例子显示了二者的不同
'''
a = str(123)
b = '123'
print(a is b, a == b)