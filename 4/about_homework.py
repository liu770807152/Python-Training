alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def solution(str):
    result, counter = {}, 0
    for item in str:
        if item in alpha:
            counter += 1
            # setdefault在执行完新增流程之后. 会根据key查询value
            value = result.setdefault(item, 0)
            value += 1
            result[item] = value

    times = sorted(list(result.values()), reverse=True)
    return times[0] / counter

print(solution('aab阿斯弗hic486dddd45864ddd9+0e上刀山rg*+^$#@&(&)@#%@@%@^(!|{}<>打赏 /q'))
