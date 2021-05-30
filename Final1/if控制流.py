def print_grade(mark):
    if mark > 0 and mark < 50:
        return 'Fail'
    elif mark >= 50 and mark < 60:
        return 'Pass'
    elif 60 <= mark < 70:
        return 'Credit'
    elif mark >= 70 and mark < 80:
        return 'Distinction'
    elif mark > 80 and mark <= 100:
        return 'High Distinction'
    else:
        return 'Invalid mark!'

'''
比较运算符的链接
你可以在 Python 中将多个比较运算符链接到一起，如此就可以创建更易读、更简洁的代码：
'''
x = 10
# Instead of:
if x > 5 and x < 15:
    print("Yes")
# You can also write:
if 5 < x < 15:
    print("Yes")


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
'''
if condition:
    x = 1
else:
    x = 0
'''
print(x)

# 函数调用也可以用这个技巧
def product(a, b):
    return a * b
def add(a, b):
    return a + b

b = True
print((product if b else add)(1, 2))