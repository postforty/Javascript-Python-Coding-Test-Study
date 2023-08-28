def calc():
    i = 0

    def add(x):
        nonlocal i
        i += x
        return i

    return add


a = calc()
print("a : ", a(1))
print("a : ", a(1))


b = calc()
print("b : ", b(2))
print("b : ", b(2))

print("a : ", a(1))
print("a : ", a(1))

print("b : ", b(2))
print("b : ", b(2))
