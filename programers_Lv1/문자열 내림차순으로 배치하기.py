# https://school.programmers.co.kr/learn/courses/30/lessons/12917?language=python3
import string
def solution(s):
    alpha_lower = string.ascii_lowercase

    first = []
    second = []

    for i in s:
        if i in alpha_lower:
            first.append(i)
        else:
            second.append(i)

    return ''.join(sorted(first, reverse=True)) + ''.join(sorted(second, reverse=True))

print(solution("Zbcdefg"))
