name = input("请输入名字:")
age = input("请输入年龄:")
job = input("请输入工作:")
hobby = input("请输入爱好:")

print("------------ info of "+name+" -----------")
print("Name  : "+name)
print("Age   : "+age)
print("job   : "+job)
print("hobby   : "+hobby)
print("------------- end -----------------")

#===========================================================
name = "Sylar"
addr = "Dota"
hobby = "选水人"

# 老的格式化方案 %d %f
print("我叫%s, 我喜欢在%s%s" % (name, addr, hobby))

# 后来的改进方法
print("我叫{0}, 我喜欢在{1}{2}".format(name, addr, hobby))

# 最方便的方法
print(f"我叫{name}, 我喜欢在{addr}{hobby}")