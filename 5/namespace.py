def f(x):
    x += y
    return x
x = 1
y = 2
z = f(x)
print(x, z, z == x)