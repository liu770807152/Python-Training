def f(ns: list):
    total = 0
    while len(ns) > 0:
        next = ns.pop(0)
        total = total + next
    return total

aList = [1, 2, 3]
print(f(aList))