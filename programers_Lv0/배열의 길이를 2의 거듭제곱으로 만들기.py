# https://school.programmers.co.kr/learn/courses/30/lessons/181857#qna
def solution(arr):
    i = 0
    while True:
        if len(arr) == 2 ** i:
            return arr
        if len(arr) < 2 ** i:
            return arr + [0] * (2 ** i - len(arr))
        i += 1

# print(solution([1, 2, 3, 4, 5, 6]))
print(solution([0, 1, 3]))
