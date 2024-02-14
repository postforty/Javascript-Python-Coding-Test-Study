# https://school.programmers.co.kr/learn/courses/30/lessons/42746?language=python3

import itertools

# 시간 초과
def solution(numbers):
    answer = ''
    
    dict = {}
    for n in numbers:
        str_n = str(n)
        if str_n[0] not in dict:
            dict[str_n[0]] = [str_n]
        else:
            dict[str_n[0]].append(str_n)

    desc_num = sorted(dict.keys(), reverse=True)

    for n in desc_num:
        max = 0
        for s in itertools.permutations(dict[n], len(dict[n])):
            num = int(''.join(s))
            if num > max:
                max = num
        answer += str(max)

    return answer

print(solution([3, 30, 34, 5, 9])) # "9534330"