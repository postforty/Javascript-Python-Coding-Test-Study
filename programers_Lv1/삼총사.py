# https://school.programmers.co.kr/learn/courses/30/lessons/131705?language=python3
import itertools

# itertools의 순열, 조합 활용
# 이 문제에서는 조합을 사용
# perm = itertools.permutations(chars, 2)  # 순열
# comb = itertools.combinations(chars, 2)  # 조합


def solution(number):
    answer = 0
    result = list(itertools.combinations(number, 3))  # 조합
    for i in result:
        if sum(i) == 0:
            answer += 1
    return answer


print(solution([-2, 3, 0, 2, -5]))  # 2
