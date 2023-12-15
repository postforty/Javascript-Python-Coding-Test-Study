# https://school.programmers.co.kr/learn/courses/30/lessons/181931?language=python3
def solution(a, d, included):
    return sum(a + i*d for i, t in enumerate(included) if t)

print(solution(3, 4, [True, False, False, True, True]))
