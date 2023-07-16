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

    result_str = "0"
    end = p + (t - 1) * m
    for i in range(1, end):
        num = ""
        quotient = i

        while quotient > 0:
            remainder = quotient % n
            num = new_num_list[remainder] + num
            quotient = quotient // n

        result_str += num

    result_str = result_str[p - 1 :: m][:t]
    return result_str


print(solution(2, 4, 2, 1))  # "0111"
