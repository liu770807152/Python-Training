# 函数连续调用
def add(x):
    class AddNum(int):
        def __call__(self, x):
            return AddNum(self.numerator + x)
    return AddNum(x)

print(add(2)(3)(5))
# 10
print(add(2)(3)(4)(5)(6)(7))
# 27
