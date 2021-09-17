sequence = [3, 9, 3, 3, 5, 9, 5]
#           0  1  2  3  4  5  6
'''
           [3, 9, 3, 3, 5, 9, 5]  index=0
           [9, 3, 3, 5, 9, 5]  index=1
           [9, 3, 5, 9, 5]  index=2
'''
print(sequence)
i = 0
while i < len(sequence):
    if sequence[i] == 3:
        sequence.pop(i)
        continue
    i += 1
print(sequence)