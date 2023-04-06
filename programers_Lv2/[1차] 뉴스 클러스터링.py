import string
import math

def solution(str1, str2):
    answer = 0

    eng = string.ascii_lowercase

    str1 = str1.lower()
    str2 = str2.lower()

    str1List = []
    str2List = []

    for i in range(len(str1) - 1):
        temp = str1[i:i+2]
        is_ok = True
        for j in temp:
            if j not in eng:
                is_ok = False
        if is_ok:
            str1List.append(temp)

    for i in range(len(str2) - 1):
        temp = str2[i:i+2]
        is_ok = True
        for j in temp:
            if j not in eng:
                is_ok = False
        if is_ok:
            str2List.append(temp)
    
    if len(str2) == 0:
        return 65536

    if len(str1) == 0:
        return 0
    
    str1List.sort()
    str2List.sort()

    if ''.join(str1List) == ''.join(str2List):
        return 65536

    # 합집합
    union_temp = str1List.copy()
    union_result = str1List.copy()

    for i in str2List:
        if i not in union_temp:
            union_result.append(i)
        else:
            union_temp.remove(i)

    union = len(union_result)

    # 교집합
    intersection_temp = []

    for i in str2List:
        if i in str1List:
            str1List.remove(i)
            intersection_temp.append(i)

    intersection = len(intersection_temp)

    answer = math.floor(intersection / union * 65536)

    return answer

print(solution("FRANCE", "french")) # 16384
# print(solution("aa1+aa2", "AAAA12")) # 43690
# print(solution("E=M*C^2", "e=m*c^2")) # 65536
# print(solution("handshake", "shake hands")) # 65536
# print(solution("", "aaa")) # 0