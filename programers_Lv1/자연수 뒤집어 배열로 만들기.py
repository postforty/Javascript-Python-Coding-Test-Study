# https://school.programmers.co.kr/learn/courses/30/lessons/12932?language=python3
def solution(n):
    return [int(el) for el in str(n)][::-1]

print(solution(12345))