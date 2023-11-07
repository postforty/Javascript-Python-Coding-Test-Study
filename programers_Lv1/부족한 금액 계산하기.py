# https://school.programmers.co.kr/learn/courses/30/lessons/82612?language=python3
def solution(price, money, count):
    answer = 0
    temp = 0

    for i in range(1, count + 1):
        temp += price * i

    result = money - temp

    if result < 0:
        return abs(result)

    return answer


print(solution(3, 20, 4))  # 10
