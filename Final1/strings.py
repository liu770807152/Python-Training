'''
Definition
'''
str = 'hello there'
print(str)
str = "hello there"
print(str)
str = '''hello there'''
print(str)
str = 'He said: "It\'s time."\n'
print(str)
print('========================================================================')
'''
ASCII
'''
print(ord('A'))
print(chr(65 + 4))
# ASCII UTF-8
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
运算符重载 operator overloading
'''
str = 'COMP'
str += '1730' # str = 'COMP' + '1730'
print(str)
long_str = str * 3
print(long_str)
# Two sequences are equal if they have the same
# length and equal elements in every position
print(long_str == str)
# seq1 < seq2 if
#   seq1 is a prefix of seq2
#   or: for some index i and the elements in each position before i are equal
print(long_str > str)
print('========================================================================')
'''
English-related operation
'''
str = 'comp1730'
print(str.lower())
print(str.upper())
str = ' I am a string string\n'
# strip() 默认是去掉字符串左右两端的空白(空格, \t, \n)
print(str.strip())
print('========================================================================')
'''
常用方法
'''
print(str.endswith('\n'))
print(str.startswith(' '))
print(str.index('a'))
print(str.split(' '))
print(str.find('str'))
print('========================================================================')
'''
Print format
'''
name = "sylar"
age = 18
s = "我叫%s, 我今年%d岁了" % (name, age)  # 了解
print(s)

s2 = f"我叫{name}, 我今年{age}岁了"  # 主推
print(s2)
print('========================================================================')
'''
looping
'''
s = "我叫周杰伦"
# while loop
i = 0
while i < len(s):
    s1 = s[i]
    print(s1, end='')
    i += 1
# for loop
s = "我叫周杰, 我也想加一个伦"
for c in s:  # 迭代循环
    print(c, end='')

if __name__ == '__main__':
    print('=================================练几道题=======================================')
    print('=================================1=======================================')
    s = 'Python rule'
    print(s[:4])
    print(s[3:-3])
    print(s[2:-2:2])
    print(s.split().sort())
