# https://school.programmers.co.kr/learn/courses/30/lessons/12977
import itertools


def solution(nums):
    answer = 0

    # 소수 판별
    def is_prime_num(n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    for i in itertools.combinations(nums, 3):
        if is_prime_num(sum(i)):
            answer += 1

    return answer


print(solution([1, 2, 3, 4]))
