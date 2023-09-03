def solution(s):
    answer = 0
    count = 1
    char = ""
    str
    for i, v in enumerate(s):
        if v == char:
            count += 1
        else:
            count = 1
            char = v

    return answer


print(solution("aaabbaccccabba"))  # 3
