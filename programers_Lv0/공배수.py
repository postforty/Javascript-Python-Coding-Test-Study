def solution(number, n, m):
    return 1 if number % n == 0 and number % m == 0 else 0

print(solution(60, 2, 3))
