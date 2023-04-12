def solution(s):
    left = 0

    if s[0] == ')' or s[-1] == "(":
        return False

    for i in s:
        if i == '(':
            left += 1
        elif i == ')':
            if left:
                left -= 1
            else:
                return False
    
    return False if left != 0 else True

print(solution("(()("))
print(solution("())(()")) # 중간에 ")("가 있는 테스트 케이스에 대한 처리 놓치지 말아야!
print(solution("()"))