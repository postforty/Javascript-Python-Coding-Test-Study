# https://school.programmers.co.kr/learn/courses/30/lessons/42586?language=python3
def solution(progresses, speeds):
    answer = []

    days_list = []
    for i, v in enumerate(progresses):
        goal = v
        days = 0
        while goal < 100:
            goal += speeds[i]
            days += 1
        days_list.append(days)
    start = days_list[0]
    cnt = 1
    for i in days_list[1:]:
        if start >= i:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            start = i
    answer.append(cnt)

    return answer

print(solution([93, 30, 55], [1, 30, 5])) # [2, 1]
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])) #	[1, 3, 2]
print(solution([90, 90, 90, 90],[30, 1, 1, 1])) #	[1, 3]
print(solution([99, 99, 99, 99, 99], [99, 99, 99, 99, 99])) # [5]
