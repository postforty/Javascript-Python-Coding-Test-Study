def outer_func():
    x = 0

    def inner_func(n):
        nonlocal x
        x += n
        return x

    return inner_func


add = outer_func()
add2 = outer_func()
print("add", add(1))
print("add2", add2(10))
print("add", add(1))
print("add2", add2(10))
print("add", add(1))
print("add2", add2(10))
