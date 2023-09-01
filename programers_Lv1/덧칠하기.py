# https://school.programmers.co.kr/learn/courses/30/lessons/161989?language=python3
# 1차 시도 : 시간 초과
# def solution(n, m, section):
#     answer = 0
#     new_section = []

#     for i, v in enumerate(section):
#         try:
#             new_section += list(range(v,section[i+1]))
#         except:
#             pass

#     new_section += section[-1:]

#     for i in section:
#         try:
#             new_section = new_section[new_section.index(i) + m:]
#             answer += 1
#         except:
#             pass

#     return answer


# 2차 시도 - 성공
def solution(n, m, section):
    answer = 1
    start = section[0]
    end = start + m - 1

    for i, v in enumerate(section[1:]):
        if end >= v:
            continue
        else:
            answer += 1
            start = v
            end = start + m - 1

    return answer


# 리팩토링
def solution(n, m, section):
    answer = 1
    end = section[0] + m - 1

    for v in section[1:]:
        if end < v:
            answer += 1
            end = v + m - 1

    return answer


print(solution(8, 4, [2, 3, 6]))  # 2
print(solution(5, 5, [3]))  # 1
print(solution(4, 2, [3, 4]))  # 1
print(solution(5, 2, [1, 4, 5]))  # 2
print(solution(4, 1, [1, 2, 3, 4]))  # 4
