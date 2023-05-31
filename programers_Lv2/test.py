def solution(citations):
    one_num = set(citations)
    if len(one_num) == 1:
        return list(one_num)[0]
    max_num = max(citations)
    for i in range(1, max_num+1):
        cnt = 0
        for j in citations:
            if j >= i:
                cnt += 1
        if cnt == i:
            return cnt

# print(solution([3, 0, 6, 1, 5])) # 3
# print(solution([1, 4, 5])) # 2
# print(solution([5, 6, 7])) # 3
print(solution([0,0,0,0,0])) # 0
print(solution([1,1,1])) # 