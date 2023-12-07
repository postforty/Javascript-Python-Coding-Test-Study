# https://school.programmers.co.kr/learn/courses/30/lessons/12935?language=python
def solution(arr):
    arr.remove(min(arr))
    return arr if len(arr) != 0 else [-1]

print(solution([4,3,2,1]))
