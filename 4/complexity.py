# 数学计算
print(1 + 1)
print('=========================================')

# 循环
l = [1, 2, 3, 4]
for item in l:
    print(item)

index = 0
while index in range(len(l)):
    print(l[index])
    index += 1
print('=========================================')

# 嵌套循环
'''
以下程序使用了嵌套循环输出2~100之间的素数：
'''
i = 2
while(i < 100):
   j = 2
   while(j <= (i / j)):
      if not(i % j):
          break
      j = j + 1
   if (j > i / j):
       print(i, " 是素数")
   i = i + 1

# 递归
'''
以下程序打印前200个斐波那契数列
'''
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

for i in range(200):
    print(i, fib(i))
print('Done!')
