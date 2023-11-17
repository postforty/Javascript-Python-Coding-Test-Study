# https://school.programmers.co.kr/learn/courses/30/lessons/17682?language=python3
def solution(dartResult):
    areas = {
        "S": "**1",
        "D": "**2",
        "T": "**3",
    }

    opts = {"~": "*2", "#": "*(-1)"}

    areas_lst = ["S", "D", "T"]
    opts_lst = ["~", "#"]
    num_lst = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    temp_dart = dartResult
    temp_dart = temp_dart.replace("10", ",@")

    for num in num_lst:
        temp_dart = temp_dart.replace(num, f",{num}")

    temp_dart_lst = temp_dart.split(",")

    for i, v in enumerate(temp_dart_lst):
        if "*" in v:
            temp_dart_lst[i] = v.replace("*", "") + "~"
            temp_dart_lst[i - 1] = temp_dart_lst[i - 1] + "~"

    dartResult = "".join(temp_dart_lst[1:])

    for num in num_lst:
        dartResult = dartResult.replace(num, f"+{num}")

    for opt in opts_lst:
        dartResult = dartResult.replace(opt, opts[opt])

    for area in areas_lst:
        dartResult = dartResult.replace(area, areas[area])

    dartResult = dartResult.replace("@", "+10")

    return eval(dartResult)


print(solution("1S2D*3T"))  # 37
print(solution("1D2S0T"))  # 3
print(solution("1D2S#10S"))  # 9
