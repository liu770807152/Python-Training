import numpy as np

# 读取该文件夹下的data.csv  comma separated value
# data = np.genfromtxt("data.csv", dtype=int, delimiter=",", skipheader=1)

# 创建一个长度为10并且除了第五个值为1的空向量
emptyVector = np.zeros(10)
emptyVector[4] = 1
print(emptyVector)
print('============================================')

# 用numpy数组检索numpy数组, 找到哪个位置的数字是1
index = np.array([0, 4, 8])
print(emptyVector[index])
isOne = (emptyVector == 1)
print(isOne)
print('============================================')

# 创建一个长度为5并且值都是10的向量
newVector = np.ones(5) * 10
print(newVector)
print('============================================')

# 创建一个值域范围从10到49的向量, 并找到它的平均值
newVector = np.arange(10, 50)
print(newVector, newVector.mean())
print('============================================')

# 深拷贝上面的向量, 并反转它(第一个元素变为最后一个)
copyVector = newVector.copy()
copyVector = newVector[::-1]
print('This is previous vector: ', newVector)
print('This is copy vector: ', copyVector)
print('============================================')

# 创建一个长度为5并且值的范围均匀分布在(-5, 5)的向量，不包括-5和5
newVector = np.linspace(-5, 5, 5)
print(newVector)
newVector = np.linspace(-5, 5, 6, endpoint=False)[1:]
print(newVector)
print('============================================')

# 创建一个 3x3 的单位矩阵, 打印它的维度等基本信息
unit = np.eye(3)
print(unit)
print(unit.ndim, unit.shape, unit.dtype)
print('============================================')

# 创建一个 2x2的随机数组, 并找到它的最大值和最小值, 并进行排序
randomVector = np.random.random((2, 2))
print(randomVector)
min, max = randomVector.min(), randomVector.max()
randomVector.sort()
print(randomVector)
print(min, max)
print('============================================')

# 创建一个 5x5的随机数组，并截取它第1到第3行、第2到第4列的数据
randomVector = np.random.random((5, 5))
print(randomVector)
randomVector = randomVector[0: 3, 1: 4]
print(randomVector)
print('============================================')