# https://school.programmers.co.kr/learn/courses/30/lessons/42746?language=python3

import itertools

def solution(numbers):
    answer = ''
    
    dict = {}
    for n in numbers:
        str_n = str(n)
        if str_n[0] not in dict:
            dict[str_n[0]] = [str_n]
        else:
            dict[str_n[0]].append(str_n)

    for n in dict.keys():
        max = 0
        for s in itertools.permutations(dict[n], len(dict[n])):
            num = int(''.join(s))
            if num > max:
                max = num
        print(max)

    return dict

print(solution([3, 30, 34, 5, 9])) # "9534330"