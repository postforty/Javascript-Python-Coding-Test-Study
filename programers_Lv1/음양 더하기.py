# https://school.programmers.co.kr/learn/courses/30/lessons/76501?language=python3
def solution(absolutes, signs):
    answer = 0
    for i, v in enumerate(signs):
        answer += -absolutes[i] if not v else absolutes[i]

    return answer


print(solution([4, 7, 12], [True, False, True]))
