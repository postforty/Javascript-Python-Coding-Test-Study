# https://school.programmers.co.kr/learn/courses/30/lessons/12906?language=python3
def solution(arr):
    temp = -1
    answer = []
    for n in arr:
        if temp != n:
            answer.append(n)
            temp =n
    return answer


print(solution([1,1,3,3,0,1,1]))
