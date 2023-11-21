# https://school.programmers.co.kr/learn/courses/30/lessons/12954?language=python3
def solution(x, n):
    answer = [x]
    new_x = x
    for i in range(1, n):
        new_x += x
        answer.append(new_x)
    return answer


print(solution(2, 5))
