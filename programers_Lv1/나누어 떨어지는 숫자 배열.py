# https://school.programmers.co.kr/learn/courses/30/lessons/12910?language=python3
def solution(arr, divisor):
    return sorted([n for n in arr if n%divisor == 0]) if len([n for n in arr if n%divisor == 0]) > 0 else [-1]

print(solution([5, 9, 7, 10], 5))
