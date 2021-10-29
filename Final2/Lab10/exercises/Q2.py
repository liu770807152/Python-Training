'''
We call a dictionary invertible if every key in it maps to a unique value, or in other words,
for every value appearing in the dictionary, there is only one key that maps to that value
'''
def is_invertible(adict):
    return sorted(adict.keys()) == sorted(adict.values())

print(is_invertible({'a' : 'b', 'b' : 'e', 'c' : 'f'}))


def is_invertible2(adict):
    d = {}
    for value in adict.values():
        if value in d:
            return False
        else:
            d[value] = 1
    return True

print(is_invertible2({'a' : 'b', 'b' : 'e', 'c' : 'f'}))
print(is_invertible2({'a' : 'b', 'b' : 'e', 'c' : 'b'}))


def invertible(adict):
    inv_dict = make_inv_dict(adict)
    return adict == inv_dict


def make_inv_dict(adict):
    if len(adict) > 0:
        # 把原输入字典修改了，结果最后原字典被清空了!!!
        key, val = adict.popitem()
        adict = make_inv_dict(adict)
        if val not in adict.values():
            adict[key] = val
        return adict
    else:
        return {}

print(invertible({ 'a' : 'b', 'b' : 'e', 'c' : 'f', 'd': 'e' }))