# https://school.programmers.co.kr/learn/courses/30/lessons/12912?language=python3
def solution(a, b):
    return sum(list(range(a, b+1))) if a < b else sum(list(range(b, a+1)))

print(solution(3, 5))
