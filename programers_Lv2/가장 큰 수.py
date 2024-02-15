# https://school.programmers.co.kr/learn/courses/30/lessons/42746?language=python3

# # 시간 초과
# import itertools

# def solution(numbers):
#     answer = ''
    
#     dict = {}
#     for n in numbers:
#         str_n = str(n)
#         if str_n[0] not in dict:
#             dict[str_n[0]] = [str_n]
#         else:
#             dict[str_n[0]].append(str_n)

#     desc_num = sorted(dict.keys(), reverse=True)

#     for n in desc_num:
#         max = 0
#         for s in itertools.permutations(dict[n], len(dict[n])):
#             num = int(''.join(s))
#             if num > max:
#                 max = num
#         answer += str(max)

#     return answer

def solution(numbers):
    # 1. 모든 수를 문자열로 변환
    numbers = list(map(str, numbers))

    # key 문자열 확인
    for x in numbers:
        print((lambda x: (x * 4))(x)[:4])

    # 2. x+y와 y+x를 비교하여 정렬
    numbers.sort(key=lambda x: (x * 4)[:4], reverse=True)

    # 3. 정렬된 numbers를 이어붙인 뒤 반환
    answer = str(int(''.join(numbers)))
    # answer = ''.join(numbers)

    return answer

# print(solution([3, 30, 34, 5, 9])) # "9534330"
print(solution([0, 0, 0])) # "9534330"
