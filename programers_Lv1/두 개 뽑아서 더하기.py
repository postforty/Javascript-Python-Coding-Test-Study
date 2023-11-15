# https://school.programmers.co.kr/learn/courses/30/lessons/68644?language=python3
import itertools


# itertools 조합을 이용한 풀이
def solution(numbers):
    answer = set()

    for i in itertools.combinations(numbers, 2):
        answer.add(sum(i))

    return sorted(list(answer))


print(solution([2, 1, 3, 4, 1]))
