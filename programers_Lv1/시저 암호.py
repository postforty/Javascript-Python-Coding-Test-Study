# https://school.programmers.co.kr/learn/courses/30/lessons/12926?language=python3
from string import ascii_lowercase, ascii_uppercase

def solution(s, n):
    answer = ''
    for c in s:
        if c in ascii_lowercase:
            idx = ascii_lowercase.find(c)+n if len(ascii_lowercase) > ascii_lowercase.find(c)+n else ascii_lowercase.find(c)+n - len(ascii_lowercase)
            answer += ascii_lowercase[idx]
        elif c in ascii_uppercase:
            idx = ascii_uppercase.find(c)+n if len(ascii_uppercase) > ascii_uppercase.find(c)+n else ascii_uppercase.find(c)+n - len(ascii_uppercase)
            answer += ascii_uppercase[idx]
        else:
            answer += c

    return answer

print(solution("a B z", 4))
print(solution("z", 1))
