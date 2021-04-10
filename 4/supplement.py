# 一般我们用is来判空
c = None
if c is None:
    print("c是空")
else:
    print("c不是空")

print('==================================')

# 关于字符串的replace()
s = '1234'
s.replace('1', str([1, 2, 3, 4]))
print(s)

s = s.replace('1', str([1, 2, 3, 4]))
print(s)