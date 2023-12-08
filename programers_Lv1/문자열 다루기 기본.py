# https://school.programmers.co.kr/learn/courses/30/lessons/12918?language=python3
def solution(s):
    answer1 = s.isdecimal()
    answer2 = len(s) == 4 or len(s) == 6
    return answer1 and answer2

print(solution("1234"))