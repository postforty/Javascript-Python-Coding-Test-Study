def solution(k, tangerine):
    d = dict()

    # 이중 for문 사용시 시간초과 발생하였음.
    for v in tangerine:
        if v not in d:
            d[v] = 1
        else:
            d[v] += 1
    
    lst = list(d.values())

    lst.sort()

    sum = 0
    cnt = 0
    while True:
        sum += lst.pop()
        cnt += 1
        if sum >= k:
            return cnt

# print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3])) # 3
print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3])) # 2