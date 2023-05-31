def solution(s):
    answer = 0
    new_s = s

    def func(t):
        if t[0] in ')}]':
            return 0
        
        a = b = c = 0
        prev = ''
        for i in range(len(t)):
            if prev == '[' and t[i] in ")}":
                return 0
            if prev == '{' and t[i] in ")]":
                return 0
            if prev == '(' and t[i] in "}]":
                return 0

            if t[i] == "[":
                a += 1
                prev = t[i]
                continue
            if t[i] == "{":
                b += 1
                prev = t[i]
                continue
            if t[i] == "(":
                c += 1
                prev = t[i]
                continue
            
            if t[i] == "]" and a > 0:
                a -= 1
            if t[i] == "}" and b > 0:
                b -= 1
            if t[i] == ")" and c > 0:
                c -= 1
            prev = t[i]

        return 1 if a + b + c == 0 else 0

    for _ in s:
        answer += func(new_s)
        new_s = new_s[1:] + new_s[:1]

    return answer


print(solution("[](){}"))  # 3
print(solution("}[](){"))  # 3
print(solution("{(})")) # 0
print(solution("}}}")) # 0
