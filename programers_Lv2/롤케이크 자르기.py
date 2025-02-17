# https://school.programmers.co.kr/learn/courses/30/lessons/132265

# 시간 초과
# def solution(topping):
#     answer = 0
    
#     for i in range(1, len(topping)-1):
#         if len(set(topping[:i])) == len(set(topping[i:])):
#             answer += 1

#     return answer

def solution(topping):
    answer = 0
    
    for i in range(1, len(topping)-1):
        if len(set(topping[:i])) == len(set(topping[i:])):
            answer += 1

    return answer
    

print(solution([1, 2, 1, 3, 1, 4, 1, 2])) # 2
print(solution([1, 2, 3, 1, 4])) # 0