# https://school.programmers.co.kr/learn/courses/30/lessons/181902?language=python3
import string

alpha = string.ascii_uppercase + string.ascii_lowercase

def solution(my_string):
    answer = []

    for i in alpha:
        answer.append(my_string.count(i))

    return answer

print(solution("Programmers"))
