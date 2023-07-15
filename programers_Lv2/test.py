# https://school.programmers.co.kr/learn/courses/30/lessons/17687?language=python3
def solution(n, t, m, p):
    num_list = [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
    ]

    new_num_list = num_list[:n]

    pre = ""
    result = ""
    count = 0
    while count < t:
        for i in new_num_list:
            result += i
            print(result)
            count += 1
            result = ""


print(solution(10, 20, 2, 1))  # "0111"
