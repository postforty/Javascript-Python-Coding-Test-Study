# https://school.programmers.co.kr/learn/courses/30/lessons/77884?language=python3
def solution(left, right):
    answer = 0

    def count_divisor(number):
        count = 0
        for i in range(1, number + 1):
            if number % i == 0:
                count += 1
        return count

    for i in range(left, right + 1):
        temp = count_divisor(i)
        if temp % 2 == 0:
            answer += i
        else:
            answer -= i

    return answer


print(solution(13, 17))
