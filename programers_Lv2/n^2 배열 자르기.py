# 테스트코드 12~20까지 시간 초과
# def solution(n, left, right):
#     answer = []

#     for i in range(1, n+1):
#         temp_lst = [i]*i
#         for j in range(i+1, n+1):
#             temp_lst.append(j)
#         answer += temp_lst
#         if len(answer) >= right:
#             return answer[left: right+1]

def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        answer.append(max(i // n, i % n) + 1)
    return answer

print(solution(3, 2, 5)) # [3,2,2,3]
print(solution(4, 7, 14)) # [4,3,3,3,4,4,4,4]
