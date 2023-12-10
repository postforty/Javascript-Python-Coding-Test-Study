# https://school.programmers.co.kr/learn/courses/30/lessons/12921?language=python3

import math
def solution(n):
    # 개선된 소수 판별 함수
    def is_prime_num(n):
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True

    answer = 0
    for i in range(2, n+1):
        if is_prime_num(i):
            answer += 1

    # return len([x for x in range(2, n+1) if is_prime_num(x)]) # 효율성 테스트 3 실패

print(solution(10))
