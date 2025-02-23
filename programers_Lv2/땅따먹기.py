# https://school.programmers.co.kr/learn/courses/30/lessons/12913
# 땅따먹기

# 1차 시도 실패
# def solution(land):
#     answer = 0

#     prev_max_index = None

#     for row in land:
#         max_value = 0
#         max_index = 0
#         for i, v in enumerate(row):
#             if prev_max_index == i:
#                 continue
#             if max_value < v:
#                 max_value = v
#                 max_index = i
#         prev_max_index = max_index
#         answer += max_value

#     return answer

# 2차 시도 실패
# def solution(land):
#     answer = 0
#     prev_max_index = None

#     for row in land:
#         if prev_max_index != None:
#             row[prev_max_index] = 0
#         answer += max(row)
#         prev_max_index = row.index(max(row))

#     return answer

# 동적 계획법(Dynamic Programming)
# DP : 메모리를 사용해서 중복 연산을 줄이고 중복 연산을 줄여서 수행 속도를 개선한다(기억하기 알고리즘, 기억하며 풀기).
def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            # land[i][j] += max(land[i-1][:]) # 이 코드는 앞에서 사용한 인덱스를 재사용하는 경우가 발생함
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])
    return max(land[-1])

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]])) # 16
