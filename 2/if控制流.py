'''交换变量
如下的小技巧很巧妙，可以为你节省多行代码：
'''
a = 1
b = 2
a, b = b, a
print(a, b) # 2 1

'''
比较运算符的链接
你可以在 Python 中将多个比较运算符链接到一起，如此就可以创建更易读、更简洁的代码：
'''
x = 10

# Instead of:
if x > 5 and x < 15:
    print("Yes")
# yes

# You can also write:
if 5 < x < 15:
    print("Yes")
# Yes

'''
条件赋值中的三元运算符
这种方法可以让代码更简洁，同时又可以保证代码的可读性：
[on_true] if [expression] else [on_false]
如以下代码：
condition = True
if condition:
    x = 1
else:
    x = 0
print(x)
可以简化成：
'''
condition = False
x = 1 if condition else 0
print(x)

# 函数调用也可以用这个技巧
def product(a, b):
    return a * b
def add(a, b):
    return a + b

b = True
print((product if b else add)(1, 2))