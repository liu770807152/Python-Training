sequence = [3.0, 1.5, 0.0, -1.5, -3.0, 3.0]

print('===========indexing===============')
print('The length of sequence is: ', len(sequence))
print('The "first" element is: ', sequence[1])
print('The "last" element is: ', sequence[-1])
'''
slicing
顾头不顾尾 [start: end]  end的数据取不到[start, end)
[start: end: step]
    start: 起始位置
    end: 结束位置(取不到)
    step: 步长. 每几个出来1个  步长如果是负数. 从右向左取. 如果是正数, 就是从左往右取数据
'''
print(sequence[1 : 6])
# length−1:−length−1:−1
sequence = []
print(sequence[len(sequence) : -len(sequence)-1 : -1])
print(sequence[1 : ]) # :后面什么都不写. 表示切到末尾
print(sequence[ : 6]) # :前面什么都不写. 表示从头开始切
print(sequence[:]) # :前后都不写. 从头到尾。以后细讲
print(sequence[ : : 2])
print(sequence[1 : : 2])
print('===========functions===============')
print(sequence.count(0.1))
print(sequence.pop())
print(sequence)
print(sequence.reverse())
print(sequence)
print(sequence.clear())
print(sequence)
