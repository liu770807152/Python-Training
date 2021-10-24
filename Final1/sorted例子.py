'''
求出现最多的英文字母的频率，忽略非英文字母
'''

alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def solution(str):
    result, counter = {}, 0
    for item in str:
        if item.isalpha():
            counter += 1
            # setdefault在执行完新增流程之后. 会根据key查询value
            tmp = result.setdefault(item, 0) + 1
            result[item] = tmp

    times = sorted(list(result.values()), reverse=True)
    print(times)
    return times[0] / counter

print(solution('aab阿斯弗hic486dddd45864ddd9+0e上刀山rg*+^$#@&(&)@#%@@%@^(!|{}<>打赏 /q'))

def getLastNum(array):
    return array[-1]

a_list = [[1, 2], [3, 4], [5, -1]]
a_list = sorted(a_list, key=getLastNum)
print(a_list)