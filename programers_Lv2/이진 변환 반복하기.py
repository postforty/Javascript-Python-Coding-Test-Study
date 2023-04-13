import re
def solution(s):
    answer = []

    temp_s = s
    count = 0
    zero = 0

    while temp_s != '1':
        zero += temp_s.count('0')
        rm_zero = re.sub('0', '', temp_s)
        temp_s = str(bin(len(rm_zero)))[2:]
        count += 1

    answer = [count, zero]

    return answer

print(solution("110010101001"))
print(solution("1111111"))
print(solution("01110"))