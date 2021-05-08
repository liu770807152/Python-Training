'''
假设我们有一个 n*n 的矩阵，矩阵中每个元素都是正数。
现在我们要从左上角走到右下角，每次只能选择向下走或者向右走，怎么走才能使得最后经过的路径上的数字之和最小？
start  1   3   5   9
       2   1   3   4
       5   2   6   7
       6   8   4   3 destination
'''
import numpy as np

data = np.array([[1, 3, 5, 9], [2, 1, 3, 4], [5, 2, 6, 7], [6, 8, 4, 3]])

def shortest_path(data):
    n = data.shape[0] # (4, 4)
    dist = np.zeros((n, n))
    sum = 0
    # 第一行只能从左边走过来
    for i in range(n):
        sum += data[0][i]
        dist[0][i] = sum
    # 记得初始化sum
    sum = 0
    # 第一列只能从上边走过来
    for i in range(n):
        sum += data[i][0]
        dist[i][0] = sum
    '''
    1   4   9   18
    3   0   0   0
    8   0   0   0
    14  0   0   0
    '''
    # 其余位置可能从上面或左边走过来
    for i in range(1, n):
        for j in range(1, n):
            dist[i][j] = min(dist[i-1, j], dist[i, j-1]) + data[i][j]
    print(dist)
    return dist[n-1][n-1]


print(shortest_path(data))