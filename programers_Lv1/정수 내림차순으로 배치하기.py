# https://school.programmers.co.kr/learn/courses/30/lessons/12933?language=python3
def solution(n):
    return int(''.join(list(map(str, sorted(map(int, list(str(n))), reverse=True)))))

print(solution(118372))