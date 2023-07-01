# https://school.programmers.co.kr/learn/courses/30/lessons/43165
import itertools


def solution(numbers, target):
    answer = 0
    sum_numbers = sum(numbers)
    temp_lst = []

    for i in range(1, len(numbers)):
        temp_lst.extend(list(itertools.permutations(numbers, i)))
    print(temp_lst)
    for t in temp_lst:
        if sum_numbers - (sum(t) * 2) == target:
            # print(t)
            answer += 1

    return answer


# print(solution([1, 1, 1, 1, 1], 3))  # 5
print(solution([4, 1, 2, 1], 4))  # 2
