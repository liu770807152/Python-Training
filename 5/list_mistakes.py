a_list = [3, 1, 2]
a_list = a_list.sort()
print(a_list)

a_list = [1, 2, 3]
b_list = a_list
a_list.append(b_list)
print(a_list)

a_list = [[]] * 3
a_list[0].append(1)
print(a_list)