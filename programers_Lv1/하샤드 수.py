# https://school.programmers.co.kr/learn/courses/30/lessons/12947?language=python3
def solution(x):
    return x % sum(map(int, list(str(x)))) == 0


print(solution(10))
