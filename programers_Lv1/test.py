def solution(ingredient):
    answer = 0
    lst = ingredient
    ref = [1, 2, 3, 1]

    i = 0
    while True:
        if len(lst) < 4:
            return answer
        if len(lst)-i < 4:
            return answer
        if lst[i:i+4] == ref:
            del lst[i:i+4]
            answer += 1
            i = 0
        else:
            i += 1
            
# print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1])) # 2
# print(solution([1, 3, 2, 1, 2, 1, 3, 1, 2])) # 0
# print(solution([1, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 1])) # 2
# print(solution([1,1,2,3,1,2,3,1,2,3,1,2,3,1])) # 3
print(solution([1,1,2,3,1,1])) # 1