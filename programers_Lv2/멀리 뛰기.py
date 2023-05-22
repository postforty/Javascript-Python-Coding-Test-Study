# from itertools import product


# def solution(n):
#     numbers = [1, 2]  # 사용할 숫자 리스트
#     target_sum = n  # 목표 합

#     result_list = []

#     # 1 또는 2가 들어가서 합이 n이 되는 모든 조합 찾기
#     for r in range(1, target_sum + 1):
#         for case in product(numbers, repeat=r):
#             if sum(case) == target_sum:
#                 result_list.append(list(case))

#     return len(result_list) % 1234567


# def solution(n):
#     if n == 1:
#         return n

#     lst = [0] * (n + 1)

#     lst[1] = 1
#     lst[2] = 2

#     for i in range(3, n+1):
#         lst[i] = (lst[i-2] + lst[i-1]) % 1234567

#     return lst[-1]

def solution(n):
    if n == 1:
        return n

    a, b = 1, 2

    for _ in range(n-2):
        a, b = b, (a+b) % 1234567

    return b

print(solution(6))  # 13
print(solution(5))  # 8
print(solution(4))  # 5
print(solution(3))  # 3
print(solution(2))  # 2
