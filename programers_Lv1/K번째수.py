# https://school.programmers.co.kr/learn/courses/30/lessons/42748?language=python3
def solution(array, commands):
    answer = []

    for lst in commands:
        temp_lst = sorted(array[lst[0] - 1 : lst[1]])
        answer.append(temp_lst[lst[2] - 1])
    return answer


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
