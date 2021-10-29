'''
Here is a function that returns the position of an element in a sequence
'''
def find_element(sq, y):
    x = 0 # index
    # this handles the case when y is not in the sequence
    if len(sq) == 0:
        return 0
    while sq[x] != y:
        x = x + 1
        # np.max returns the maximum number in an array
        if x < len(sq):
            x = x + 1 - 1 # don't want to change i again
        else:
            return x
    # this is the end of the loop
    return x


print(find_element([1, 2, 3, 4, 5], 4))

'''
1. 先从命名开始：sq既然是sequence，就应该更名成seq/sequence；x既然是index，就应该命名成index，而不是写注释额外说明；y既然是要查找的元素，就应该命名成terget/target_element(注意多单词要用_连接)
2. 再从注释入手：
    2.1 没有docstring，应该补上，如：Return the position of element target in the sequence seq. If target is not present, return the sequence length.
    2.2 行内注释部分： 
        2.2.1 Line6的注释有误：应该是处理传入的sequence为空的情况
        2.2.2 Line11的注释明显过时，删掉，或者改成while循环的说明
3. 然后发现Line12-15的代码是多余代码，应该改成：
    if i >= len(seq):
        return i # this is the end of the loop
4. "# this is the end of the loop"不够好，可以改成：# reaching the end, target is not found
4. 都改完后，再看看循环部分能不能优化：
    while seq[i] != target:
        i = i + 1
        if i >= len(seq):
            return i # reaching the end, target is not found
    明显存在多余的逻辑，应该一找到target就返回，如：
    for index in range(len(seq)):
        if seq[index] == target:
            return index
'''