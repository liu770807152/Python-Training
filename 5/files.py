# r:  read 只读模式.
f = open("a.txt", mode="r", encoding='utf-8')
# 1.read() 直接全部读取出来. 内存容易炸
print(f.read())
# 2.readline()  一次读取一行
print(f.readline())
print(f.readline())
# 3.for循环(重点)
for line in f:  # 每次循环读取一行内容
    print(line.strip())  # 去掉换行
# 4.前面一行单独读取, 后面数据用for循环
first = f.readline()
print(first)
print("===========")
for line in f:
    print(line)
print("=================================================")

# w: write 只写模式, 重新创建文件
f = open("b.txt", mode="w", encoding="utf-8")
f.write("周杰伦")
f.write("\n")  # 换行
f.write("哈哈")

# a: append 追加写. 不会重新创建文件, 但是如果文件不存在, 可以创建文件
f = open("c.txt", mode="a", encoding="utf-8")
f.write("你好")

# b: bytes, 二进制  一般处理非文本文件, 不能指定encoding
# rb 读取字节
# wb 写入字节
f1 = open("pumpkin.jpg", mode="rb")
f2 = open("newPumpkin.jpg", mode="wb")
for line in f1:
    f2.write(line)

# +: 扩展  r+ w+ a+, r+b w+b a+b
f = open("a.txt", mode="r+", encoding='utf-8')
print(f.read())
f.write("后天天气不好")
f.close()

# 另一种写法, 可以省略掉close
with open("a.txt", mode="r", encoding="utf-8") as f1, \
     open("d.txt", mode="w", encoding='utf-8') as f2:
    for line in f1:
        f2.write(line)

'''
文件修改操作
读取文件中的内容
把要修改的内容进行修改
把新内容写入到一个副本文件中

必须借助os模块
把原来的文件删除掉
把新文件重命名成原来的文件名
'''
import os

with open("f.txt", mode="r", encoding="utf-8") as f1, \
     open("f_副本.txt", mode="w", encoding="utf-8") as f2:
    for line in f1:
        if "人" in line:
            line = line.replace("人", "阿拉斯加")
        f2.write(line)
os.remove("f.txt")  # 删除源文件
os.rename("f_副本.txt", "f.txt")  # 把副本文件重命名成源文件


# 读取规则的文件
f = open("a.txt", mode="r", encoding="utf-8")
head_str = f.readline()
# 把头处理成列表
head_list = head_str.split()  # 默认的split()用空白切割
print(head_list)
lst = []
for line in f:
    line = line.strip()  # 去掉左右两端空白
    data_list = line.split()  # 切割
    print(data_list)
    dic = {}
    for i in range(len(head_list)):  # 拿到索引
        dic[head_list[i]] = data_list[i]  # 向字典中填充数据
    lst.append(dic)
print(lst)
f.close()