# def find_max(x, y):
#    d = 0
#    for i in x and j in y:
#        d = max(d, i - j)
#    return d

# print("The max difference is ", find_max([1, 2, 3], [1, 2, 3]))


def find_max(y):
    z = x[0] * y
    for i in range(len(x)):
        x[i] = y * x[i]
        if x[i] > z:
            z = x[i]
    return z

x = [1, 2, 3]
print("The max value is ", find_max(1))
print("The min value is ", find_max(-1))
print("The max difference is ", find_max(1) - find_max(-1))


def find_a_max(x):
    # x becomes None!!!
    x = x.sort()
    return x[-1] - x[1]

print("The max difference is ", find_a_max([1, 2, 3]))