# https://school.programmers.co.kr/learn/courses/30/lessons/154538
# 숫자 변환하기

'''
10
+5          *2          *3
-------------------------------------------
15          20          30          |   1회
20  30  45  25  40  60  35  60  90  |   2회
'''

# 테스트 5, 7, 9, 10, 11 시간 초과
# def func(x, y, n):
#     temp = [x + n, x * 2, x * 3]
#     if y in temp:
#         return [y]
#     return temp
    
# def solution(x, y, n):
#     answer = 0

#     if x == y: return answer

#     tabu = func(x, y, n)
#     temp = []
    
#     while tabu:
#         if min(tabu) > y:
#             return -1
        
#         answer += 1
        
#         if y in tabu:
#             return answer
        
#         for num in tabu:
#             temp += func(num, y, n)
#             if y in temp:
#                 return answer + 1
        
#         tabu = temp
#         temp = []

#     return answer

# 테스트 5, 7, 9, 10, 11 시간 초과
# def func(x, y, n):
#     temp = [x + n, x * 2, x * 3]
#     if y in temp:
#         return [y]
#     return temp
    
# def solution(x, y, n):
#     answer = 0

#     if x == y: return answer

#     tabu = func(x, y, n)
#     temp = []
    
#     while tabu:       
#         answer += 1
        
#         if y in tabu:
#             return answer
        
#         for num in tabu:
#             temp += [n for n in func(num, y, n) if n <= y] # 수정
#             if y in temp:
#                 return answer + 1
        
#         tabu = temp
#         temp = []

#     return -1 # 수정

# DP 사용하여 해결
def solution(x, y, n):
    if x == y:
        return 0
    
    dp = [float('inf')] * (y + 1)
    dp[x] = 0  # 시작점은 연산 0회
    
    for i in range(x, y + 1):
        if dp[i] == float('inf'): # inf는 양의 무한대
            continue  # 도달 불가능한 숫자는 건너뜀

        # 가능한 연산 수행
        if i + n <= y:
            dp[i + n] = min(dp[i + n], dp[i] + 1)
        if i * 2 <= y: # 조건식 때문에 dp 리스트 범위를 벗어나는 일은 없음
            dp[i * 2] = min(dp[i * 2], dp[i] + 1)
        if i * 3 <= y:
            dp[i * 3] = min(dp[i * 3], dp[i] + 1)

    return dp[y] if dp[y] != float('inf') else -1

print(solution(10, 40, 5)) # 2
print(solution(10, 40, 30)) # 1
print(solution(2, 5, 4)) # -1