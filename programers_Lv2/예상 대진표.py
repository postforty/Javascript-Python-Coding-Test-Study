def solution(n,a,b):
    answer = 0

    lst = [0] * n
    lst[a-1] = 1
    lst[b-1] = 2

    def func(param):
        new_lst = []
        while lst:
            a = param.pop()
            b = param.pop()
            new_lst.append(a + b)
        return new_lst
    
    while True:
        lst = func(lst)
        answer += 1
        if max(lst) > 2:
            break

    return answer

print(solution(8, 4, 7)) # 3
print(solution(8, 3, 7)) # 3
print(solution(8, 2, 7)) # 3


 