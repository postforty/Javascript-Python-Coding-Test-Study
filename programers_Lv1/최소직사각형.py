def solution(sizes):
    a = b = 0
    for i in sizes:
        i.sort()
        x, y = i
        a = x if x > a else a
        b = y if y > b else b
    return a * b


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
