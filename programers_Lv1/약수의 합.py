# https://school.programmers.co.kr/learn/courses/30/lessons/12928?language=python3
def solution(n):
    return sum([el for el in range(1, n+1) if n % el == 0])

print(solution(12))