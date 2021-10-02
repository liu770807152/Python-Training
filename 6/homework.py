import numpy as np

def index_ranker(l):
    temp_list = l[:]
    result = []
    temp_list.sort(reverse=True)
    for num in l:
        result.append(temp_list.index(num) + 1)
    return result

def handle_duplicates(l):
    count = dict()
    for num in l:
        if num in count.keys():
            count[num] += 1
        else:
            count[num] = 1
    for key, value in count.items():
        if value > 1:
            new_average = np.average([key + i for i in range(value)])
            l = [new_average if num == key else num for num in l]
            #for num in l:
            #    if num == key:
            #        num = new_average
            #    else:
            #        num = num
    return l

if __name__=='__main__':
    print(handle_duplicates(index_ranker([2, 4, 6])))
    print(handle_duplicates(index_ranker([-1, 0, 1])))
    print(handle_duplicates(index_ranker([4, 6, 2])))
    print(handle_duplicates(index_ranker([0, -1, 1])))
    print(handle_duplicates(index_ranker([6, 2, 4])))
    print('=========================================')
    print(handle_duplicates(index_ranker([2, 2, 6, 6])))
    print(handle_duplicates(index_ranker([2, 2, 2, 2])))
    print('=========================================')
    print(handle_duplicates(index_ranker([0, 0, 0, 0])))
    print(handle_duplicates(index_ranker([1, 1, 1, 1])))
    print(handle_duplicates(index_ranker([1.5, 1.6, 1.5, 1.5])))
