# https://school.programmers.co.kr/learn/courses/30/lessons/84512
# 모음 사전
import itertools

# [참고] itertools.product()
# 두개 이상의 리스트(or 집합) 끼리의 데카르트 곱(cartesian product)를 계산하여 iterator로 반환해준다. Cartesian Product는 아래와 같이 정의된다.
# A = [1,2,3]
# list(itertools.product(A, repeat=2)) # [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]

# [이하 문제 풀이]

# def solution(word):
#     vowels = ['A', 'E', 'I', 'O', 'U']
#     words = [] 
#     for i in range(1, 6):
#         for comb in itertools.product(vowels, repeat=i): # 첫번째 인자로 리스트
#             words.append(''.join(comb))
#     words.sort()
#     return words.index(word) + 1
    
# def solution(word):
#     words = []  
#     for i in range(1, 6):
#         for comb in itertools.product('AEIOU',  repeat=i): # 첫번째 인자로 문자열
#             words.append(''.join(comb))
#     words.sort()
#     return words.index(word) + 1

def solution(word):
    return sorted(["".join(w) for i in range(1, 6) for w in itertools.product('AEIOU', repeat=i)]).index(word) + 1

print(solution("AAAAE")) # 6
# print(solution("AAAE")) # 10
# print(solution("I")) # 1563
# print(solution("EIO")) # 1189