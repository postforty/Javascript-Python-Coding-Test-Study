# https://school.programmers.co.kr/learn/courses/30/lessons/136798?language=python3
import math

def solution(number, limit, power):
    answer = 0

    for n in range(1, number + 1):
        count = 0
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                count += 1
                if i != n // i:
                    count += 1
        if count > limit:
            count = power
        answer += count

    return answer


print(solution(10, 3, 2))  # 21
