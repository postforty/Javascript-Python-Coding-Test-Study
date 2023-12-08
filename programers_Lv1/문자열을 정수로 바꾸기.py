# https://school.programmers.co.kr/learn/courses/30/lessons/12925
def solution(s):
    s_str = str(s)
    prefix = s_str[0] if s_str[0] == "+" or s_str[0] == "-" else ''
    value = s_str[1:] if s_str[0] == "+" or s_str[0] == "-" else s_str[:]
    return int(prefix + value)

print(solution(-1234))