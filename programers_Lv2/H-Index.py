def solution(citations):
    s_c = sorted(citations, reverse=True)
    num = s_c[0]
    for i in range(num, 0, -1):
        cnt = 0
        for j in s_c:
            if j >= i:
                cnt += 1
                if i == cnt:
                    return cnt
    return 0
print(solution([3, 0, 6, 1, 5])) # 3
print(solution([1, 4, 5])) # 2
print(solution([5, 6, 7])) # 3
# print(solution([0,0,0,0,0])) # 0
# print(solution([1,3,1])) # 1
print(solution([25, 8, 5, 3, 3])) # 3