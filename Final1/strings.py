'''
Definition
'''
str = 'hello there'
print(str)
str = "hello there"
print(str)
str = '''hello there'''
print(str)
str = 'He said: \"It\'s time.\"\n'
print(str)
print('========================================================================')
'''
ASCII
'''
print(ord('A'))
print(chr(65 + 4))
print(chr(20986) + chr(21475))
print('========================================================================')
'''
Indexing & length
顾头不顾尾 [start: end]  end的数据取不到[start, end)
[start: end: step]
    start: 起始位置
    end: 结束位置(取不到)
    step: 步长. 每几个出来1个  步长如果是负数. 从右向左取. 如果是正数, 就是从左往右取数据
'''
str = 'Hello world!'
print(len(str))
print(str[1])
print(str[-1])
print(str[1 : 6])
print(str[-5 : -1])
print(str[1 : ]) # :后面什么都不写. 表示切到末尾
print(str[ : 6]) # :前面什么都不写. 表示从头开始切
print(str[:]) # :前后都不写. 从头到尾。以后细讲
print(str[ : : 2])
print('========================================================================')
'''
English-related operation
'''
print(str.capitalize())
print(str.lower())
print(str.upper())
str = ' I am a string\n'
# strip() 默认是去掉字符串左右两端的空白(空格, \t, \n)
print(str.strip())
print('========================================================================')
'''
conditional judgement
'''
money = '123456'
print(money.isdigit())
money = 'l23456'
print(money.isdigit())
print('========================================================================')
# 关于字符串的replace()
str = '12341'
str.replace('1', '0')
# nothing happen?
print(str)
str = str.replace('1', '0')
print(str)
print('==========================变量名是str, 那str函数还能用吗？==============================')
# str = str(123)