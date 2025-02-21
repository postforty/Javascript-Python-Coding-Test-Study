# https://school.programmers.co.kr/learn/courses/30/lessons/131704
# 택배상자

# 정확성 실패
# def solution(order):
#     answer = 1
#     pointer = order[0]
#     stack = [pointer-1]

#     for i in order[1:]:
#         pointer += 1
#         if i == pointer:
#             answer += 1
#         elif stack and i < pointer and i == stack[-1]:
#             answer += 1
#             stack.append(stack.pop()-1)
#         else:
#             stack.append(pointer)

#     return answer

def solution(order):
    answer = 0
    stack = []
    current = 1

    for box in order:
        while current <= box:
            stack.append(current)
            current += 1
        if stack[-1] == box:
            stack.pop()
            answer += 1
        else:
            break

    return answer

print(solution([4, 3, 1, 2, 5])) # 2
print(solution([5, 4, 3, 2, 1])) # 5
print(solution([5])) # 5