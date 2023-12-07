# https://school.programmers.co.kr/learn/courses/30/lessons/12934
import math

def solution(n):
    return -1 if math.sqrt(n) % 1 > 0 else int((math.sqrt(n)+1)**2)

print(solution(3))
