# https://school.programmers.co.kr/learn/courses/30/lessons/181936?language=python3
def solution(number, n, m):
    # 공배수
    return 1 if number % n == 0 and number % m == 0 else 0

print(solution(60, 2, 3))
