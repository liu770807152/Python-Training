import numpy as np
import matplotlib.pyplot as plt

'''
绘制一个函数的散点图
'''
N = 50
x = np.linspace(0., 10., N)
y = np.sin(x)**2 + np.cos(x)
# 变量 x 是从 0 到 10 的 50 个数据的数组。
# 变量 y 是 sin（x） 和 cos（x） 的平方之和。
# 为了使其更美观，可以减少每个数据的大小并给标签添加下面的代码
# 要更改颜色，需要在代码中添加 color 参数
plt.scatter(x, y, s = 15, color = 'r', label = r'$y  = sin^2(x) + cos(x)$')
# 如果要使轴比例尺相同，可以使用下面的代码
plt.axis('equal')
# 要为 x 轴和 y 轴创建轴标签，可以添加以下代码
plt.xlabel(r'$x$ (rad)')
plt.ylabel(r'$y$')
# 要显示图例，可以使用下面的代码
plt.legend()
# 要保存图形，可以使用以下代码
plt.savefig('./graphs/scatter2.png', dpi = 300, bbox_inches = 'tight', facecolor='w')
plt.show()

'''
绘制不同颜色标注的散点图
'''
np.random.seed(100)

N = 30
randx = np.random.random(N) * 100
randy = np.random.random(N) * 100
ranking = np.random.random(N) * 200
# 为 50 到 200 之间的每个数据生成一个随机整数
size = np.random.randint(50, 200, size=N)

plt.figure(figsize=(7, 5))
plt.scatter(randx, randy, s = size, c = size, alpha = .8)
plt.axis('equal')

# 需要在 x 轴和 y 轴上插入次刻度。
# 要插入它，需要使用以下代码导入子模块 MultipleLocator
from matplotlib.ticker import MultipleLocator
# 插入辅助轴
ax = plt.gca()
ax.xaxis.set_minor_locator(MultipleLocator(10))
ax.yaxis.set_minor_locator(MultipleLocator(10))

plt.xlabel('randx')
plt.ylabel('randy')

plt.colorbar()
plt.show()

'''
绘制线图
'''
N = 50
x = np.linspace(0., 10., N)
y = np.sin(x)**2 + np.cos(x)
# 线条图的线条样式：['-', '--', '-.', ':']
linestyles = ['-', '--', '-.', ':']

rows = 2
columns = 2
grid = plt.GridSpec(rows, columns, wspace = .25, hspace = .25)
plt.figure(figsize=(15, 10))
# 一次性画出4张不同样式的线图
for i in range(len(linestyles)):
    # 当前画第几张图
    plt.subplot(grid[i])
    # 线条宽度
    plt.plot(x, y, linestyle = linestyles[i], lw = 2.0, label = r'$ y  = sin^2(x) + cos(x)$')
    plt.axis('equal')
    plt.xlabel('$x$ (rad)')
    # plt.legend()
    # 添加注释
    plt.annotate("linestyle '" + str(linestyles[i]) + "'", xy = (0.5, -2.5), va = 'center', ha = 'left')
plt.show()

'''
创建添加误差的线形图
'''
N = 25
x = np.linspace(0., 10., N)
y = np.sin(x)**2 + np.cos(x)

np.random.seed(100)
noise_x = np.random.random(N) * .2 + .1
noise_y = np.random.random(N) * .7 + .4

plt.figure(figsize=(7, 4.5))
plt.errorbar(x, y, yerr = noise_y, xerr = noise_x, label = r'$ y  = sin^2(x) + cos(x)$')
plt.axis('equal')
plt.legend()
plt.xlabel('$x$ (rad)')
plt.show()
# 如果只想显示误差线，则可以使用以下参数
plt.errorbar(x, y, xerr = noise_x, yerr = noise_y, label = r'$ y  = sin^2(x) + cos(x)$', color = 'r', fmt = 'o', ecolor='k', )
plt.axis('equal')
plt.legend()
plt.xlabel('$x$ (rad)')
plt.show()

'''
竖直柱状图
'''
N = 1000
np.random.seed(10021)
x = np.random.randn(N) * 2 + 15

plt.figure(figsize=(9, 6))
plt.hist(x, bins = 40, range = (12, 18), color = 'darkorange', label = r'$\mu = 15, \sigma = 2$')
plt.legend()
plt.show()

'''
水平柱状图
'''
x = np.random.randn(N) * 2 + 15

plt.figure(figsize=(9, 6))
plt.hist(x, bins = 25, range = (12, 18), color = 'royalblue', orientation='horizontal',  edgecolor='k', label = r'$\mu = 15, \sigma = 2$')
plt.legend()
plt.show()

'''
叠放的柱状图
'''
mu1 = 5
mu2 = 10
mu3 = 15

sigma1 = 5
sigma2 = 3
sigma3 = 2

x1 = np.random.randn(N) * sigma1 + mu1
x2 = np.random.randn(N) * sigma2 + mu2
x3 = np.random.randn(N) * sigma3 + mu3

plt.figure(figsize=(9, 6))
# alpha添加透明度
plt.hist(x1, bins = 30, color = 'royalblue', label = r'$\mu = $ ' + str(mu1) + ', $\sigma = $ ' + str(sigma1), alpha = .7, edgecolor='k',)
plt.hist(x2, bins = 30, color = 'tomato', label = r'$\mu = $ ' + str(mu2) + ', $\sigma = $ ' + str(sigma2), alpha = .7, edgecolor='k',)
plt.hist(x3, bins = 30, color = 'gray', label = r'$\mu = $ ' + str(mu3) + ', $\sigma = $ ' + str(sigma3), alpha = .7, edgecolor='k',)
plt.legend()

'''
竖直条形图
'''
name = ['Adam', 'Barry', 'Corbin', 'Doe', 'Evans', 'Frans']

np.random.seed(100)
N = len(name)
math = np.random.randint(60, 100, N)

plt.figure(figsize=(9, 6))
plt.bar(name, math, alpha = .7)
plt.ylabel('Math Exam')
plt.show()

'''
水平条形图+误差线
'''
name = ['Adam', 'Barry', 'Corbin', 'Doe', 'Evans', 'Frans']
course_name = ['Math', 'Physics', 'Biology', 'Chemistry']
colors = ['#00429d', '#7f40a2', '#a653a1', '#c76a9f',
          '#e4849c', '#d0e848']

N = len(name)
rows = 2
columns = 2
plt.figure(figsize=(12, 8))
grid = plt.GridSpec(rows, columns, wspace = .25, hspace = .25)
np.random.seed(100)

for i in range(len(course_name)):
    course = np.random.randint(60, 95, N)
    noise = np.random.randint(1, 3, N)
    plt.subplot(grid[i])
    plt.barh(name, course, color = colors, xerr = noise,
             ecolor = 'k')
    plt.xlabel(course_name[i] + ' Exam')
    plt.xlim(60, 100)
    plt.gca().invert_yaxis()
plt.show()