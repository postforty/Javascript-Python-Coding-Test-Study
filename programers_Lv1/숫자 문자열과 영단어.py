# https://school.programmers.co.kr/learn/courses/30/lessons/81301?language=python3
def solution(s):
    answer = s
    words = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]

    for i, v in enumerate(words):
        if v in s:
            answer = answer.replace(v, str(i))
    return int(answer)


print(solution("one4seveneight"))  # 1478
