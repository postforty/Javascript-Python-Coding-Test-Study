# https://school.programmers.co.kr/learn/courses/30/lessons/86051?language=python3
def solution(numbers):
    answer = 0

    for i in range(0, 10):
        if i not in numbers:
            answer += i
    return answer


print(solution([1, 2, 3, 4, 6, 7, 8, 0]))
