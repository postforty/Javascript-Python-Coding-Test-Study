def solution(s):
    answer = 0
    new_s = s

    def func(t):
        if t[0] in "])}":
            return "stop"

        a = b = c = 0
        for i in range(len(t)):
            if a > 1:
                if t[i] in ")}":
                    return "stop"
            if b > 1:
                if t[i] in ")]":
                    return "stop"
            if c > 1:
                if t[i] in "}]":
                    return "stop"
            if t[i] == "[":
                a += 1
                continue
            if t[i] == "{":
                b += 1
                continue
            if t[i] == "(":
                c += 1
                continue
            if t[i] == "]" and a > 0:
                a -= 1
            if t[i] == "}" and b > 0:
                b -= 1
            if t[i] == ")" and c > 0:
                c -= 1

        return 1 if a + b + c == 0 else 0

    for _ in s:
        if func(new_s) != "stop":
            return 0
        else:
            answer += func(new_s)
        new_s = new_s[1:] + new_s[:1]

    return answer


print(solution("[](){}"))  # 3
# print(solution("}[](){"))  # 3
# print(solution("{(})"))
