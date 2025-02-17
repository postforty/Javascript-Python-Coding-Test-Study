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

    left = {}
    for i in topping:
        if i in left:
            left[i] += 1
        else:
            left[i] = 1

    right = {}

    # 순회하면서 오른쪽에 토핑을 하나씩 나눠줌
    for t in topping:
        if t in right:
            right[t] += 1
        else:
            right[t] = 1
            
        left[t] -= 1
        
        # 왼쪽에 해당 토핑 값이 0이면 키 삭제
        if not left[t]:
            del(left[t])
        
        # 왼쪽 토핑(키) 갯수 == 오른쪽 토핑(키) 갯수 같으면 1 더함
        if len(left) == len(right):
            answer += 1
    
    return answer
    

print(solution([1, 2, 1, 3, 1, 4, 1, 2])) # 2
print(solution([1, 2, 3, 1, 4])) # 0