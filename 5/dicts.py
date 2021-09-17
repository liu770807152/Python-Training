# key可以是任何object，但是要保证不一样！！！！
# Keys must be immutable
d = {123: "呵呵", True: "哈哈", "name": "me", (1,2,3): 123}
print(d)
print('====================================')

'''search'''
print(d[(1,2,3)])  # 通过key找value
# setdefault在执行完新增流程之后. 会根据key查询value
print(d.setdefault(123))
print('====================================')
# 循环遍历
# 1.直接for循环, 直接拿到key, 记住
for k in d:
    print(k)
    print(d[k])
print('====================================')

# 2. 借助字典的keys() 了解
print(d.keys())
for k in d.keys():
    print(k)
    print(d[k])
print('====================================')

# 3. 拿到所有的value
for v in d.values():
    print(v)
print('====================================')

# 4. 通过items()拿到所有数据, 最直接的拿到k和v的方案
print(d.items())
for k, v in d.items():
    print(k)
    print(v)
print('====================================')

'''add'''
d['key'] = "随便"
print(d)
print('====================================')

'''alter'''
d['name'] = 'James'
print(d)
print('====================================')

'''delete'''
print(d.pop(123))
print(d)
del d[True]
print(d)
d.clear()
print(d)
print('====================================')

'''反转字典'''
m = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
newMap = {v: k for k, v in m.items()} # {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
print(newMap)
print('====================================')

''' 
    练习: [11,22,33,44,55,66,77,88,99]
    分类, 把大于55的放一起, 把小于55的放一起
    结果: {"bigger":[66,77,88,99], "smaller":[11,22,33,44,55]}
'''

# l = [11, 22, 33, 44, 55, 66, 77, 88, 99]
# result = {}
# for item in l:
#     if item > 55:
        # setdefault在执行完新增流程之后. 会根据key查询value
#         result.setdefault("bigger", []).append(item)
#     else:
        # setdefault在执行完新增流程之后. 会根据key查询value
#         result.setdefault("smaller", []).append(item)
# print(result)

'''dict的嵌套'''
wang = {
    "name": "汪峰",
    "wife": {
        "name": "章子怡",
        "age": 18,
        'hobby': ['台球', "武术", "演戏"]
    },
    "hobby": ["唱歌", '跳舞', "当导师"],
    "children": [
        {"name": "老大", "age": 10},
        {"name": "老二", "age": 8},
    ]
}

# 练习：
# 1. 给汪峰的二儿子加一岁
wang['children'][1]['age'] += 1
print(wang)
# 2. 给汪峰添加一个爱好: 卡拉ok
wang['hobby'].append('卡拉ok')
print(wang)
# 3. 检查汪峰老婆有没有“武术”的爱好
print('有' if '武术' in wang['wife']['hobby'] else '没有')

'''
难点的代码
'''
a_dict = {1: [0], 2: [1]}
b_dict = a_dict
c_dict = a_dict.copy()
b_dict[1] = [2]
c_dict[1] = [0, 0]
a_dict[2].append(1)