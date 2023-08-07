# https://school.programmers.co.kr/learn/courses/30/lessons/138477
def solution(k, score):
    answer = []
    temp = []

    for i in score:
        if len(temp) == 0:
            temp.append(i)
            answer.append(i)
            continue
        if len(temp) <= k:
            temp.append(i)
            temp.sort()
            answer.append(temp[0])
            continue
        if temp[0] < i:
            temp[0] = i
            temp.sort()
            answer.append(temp[0])
        else:
            answer.append(temp[0])

    return answer


print(solution(3, [10, 100, 20, 150, 1, 100, 200]))  # [10, 10, 10, 20, 20, 100, 100]
