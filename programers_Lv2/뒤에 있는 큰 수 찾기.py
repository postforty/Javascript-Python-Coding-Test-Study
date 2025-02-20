# https://school.programmers.co.kr/learn/courses/30/lessons/154539
# 뒤에 있는 큰 수 찾기

# 시간 초과
# def solution(numbers):
#     length = len(numbers)

#     answer = [-1] * length
#     stack = []

#     for i in range(length):
#         j = 0
#         while stack:
#             if stack[-1] + j >= length:
#                 stack.pop()
#                 break
#             elif numbers[stack[-1]] < numbers[stack[-1] + j]:
#                 answer[stack.pop()] = numbers[stack[-1] + j]
#             else:
#                 j += 1
                
#         if not stack:
#             stack.append(i)

#     return answer

def solution(numbers):
    length = len(numbers)
    answer = [-1] * length
    stack = []

    for i in range(length):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
        
        # print(stack)

    return answer

print(solution([2, 3, 3, 5])) # [3, 5, 5, -1]
print(solution([9, 1, 5, 3, 6, 2])) # [-1, 5, 6, 6, -1, -1]