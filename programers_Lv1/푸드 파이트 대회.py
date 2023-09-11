# https://school.programmers.co.kr/learn/courses/30/lessons/134240?language=python3
def solution(food):
    answer = ""

    for i, v in enumerate(food[1:]):
        answer += str(i + 1) * (v // 2)

    return answer + "0" + answer[::-1]


print(solution([1, 3, 4, 6]))  # 1223330333221
