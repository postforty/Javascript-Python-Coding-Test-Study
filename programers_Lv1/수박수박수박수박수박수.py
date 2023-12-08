# https://school.programmers.co.kr/learn/courses/30/lessons/12922?language=python3
def solution(n):
    s_list = ['수', '박']
    answer = ''
    for i, v in enumerate(range(n)):
        if i % 2 == 0:
            answer+=s_list[0]
        else:
            answer+=s_list[1]
    return answer

print(solution(3))