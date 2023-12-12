# https://school.programmers.co.kr/learn/courses/30/lessons/12903?language=python3
def solution(s):
    return s[len(s) // 2] if len(s) % 2 != 0 else s[len(s) // 2 - 1:len(s) // 2 + 1]

print(solution("abcde"))
print(solution("qwer"))
