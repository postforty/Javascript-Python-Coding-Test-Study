# https://school.programmers.co.kr/learn/courses/30/lessons/43165
def solution(numbers, target):
    answer = 0

    for i, v in enumerate(numbers):
        temp_sum = sum(numbers)
        temp_sum -= v * 2
        if temp_sum < target:
            continue
        if temp_sum == target:
            answer += 1

    return answer


print(solution([1, 1, 1, 1, 1], 3))  # 5
