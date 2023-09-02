# https://school.programmers.co.kr/learn/courses/30/lessons/147355?language=python3
def solution(t, p):
    answer = 0
    slice_length = len(p)
    i = 0
    while True:
        temp = t[i : slice_length + i]
        if len(temp) < slice_length:
            break
        if int(temp) <= int(p):
            answer += 1
        i += 1

    return answer


# print(solution("3141592", "271"))  # 2
print(solution("500220839878", "7"))  # 8
