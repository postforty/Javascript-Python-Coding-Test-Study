# https://school.programmers.co.kr/learn/courses/30/lessons/12943?language=python3
# 콜라츠 추측
def solution(num):
    count = 0
    while True:
        if num == 1:
            return count
        if count >= 500:
            return -1
        if num % 2 == 0:
            num /= 2
        else:
            num *= 3
            num += 1
        count += 1


print(solution(6))
