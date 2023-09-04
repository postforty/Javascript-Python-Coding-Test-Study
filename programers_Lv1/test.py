def solution(s):
    answer = []
    count = 1
    char = s[0]
    str_result = char
    for i, v in enumerate(s[1:]):
        if count != 0:
            if char == v:
                count += 1
            else:
                count -= 1
                char = v
            str_result += v
        if count == 0:
            answer.append(str_result)
            count = 1
            str_result = v
        print(count)

    return answer


print(solution("aaabbaccccabba"))  # 3
# print(solution("ab"))  # 3
