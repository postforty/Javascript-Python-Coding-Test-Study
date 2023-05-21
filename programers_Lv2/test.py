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


def solution(n):
    temp = dict()
    temp[0] = 1
    temp[1] = 1
    print(temp)
    dp = [0] * (n + 1)
    dp[1] = 1
    if n == 1:
        return 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = (dp[i - 2] + dp[i - 1]) % 1234567
        print(dp)

    return dp[n]


print(solution(4))  # 5
# print(solution(3))  # 3
