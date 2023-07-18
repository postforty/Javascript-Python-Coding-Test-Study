# https://school.programmers.co.kr/learn/courses/30/lessons/42626
# 1차 시도 - 일부 테스트 케이스 → 실패, 효율성 테스트 모두 → 실패
# def solution(scoville, K):
#     answer = 0
#     sorted_scoville = sorted(scoville)
#     temp_sorted_scoville = [n for n in sorted_scoville if n <= K]

#     try:
#         sorted_scoville = temp_sorted_scoville + [
#             sorted_scoville[len(temp_sorted_scoville)]
#         ]
#     except:
#         sorted_scoville = temp_sorted_scoville

#     sorted_scoville = sorted(sorted_scoville, reverse=True)

#     check = -1
#     while sorted_scoville:
#         try:
#             a = sorted_scoville.pop()
#             b = sorted_scoville.pop()
#         except:
#             return check if check == -1 else answer
#         else:
#             r = a + (b * 2)
#             if r < K:
#                 sorted_scoville.append(r)
#                 sorted_scoville = sorted(sorted_scoville, reverse=True)
#                 answer += 1
#             else:
#                 answer += 1
#                 check += 1

#     return answer


# 2차 시도 - 효율성 테스트 → 실패
# def solution(scoville, K):
#     answer = 0
#     sorted_scoville = sorted(scoville)

#     while sorted_scoville[0] < K:
#         if len(sorted_scoville) < 2:
#             return -1

#         a = sorted_scoville.pop(0)
#         b = sorted_scoville.pop(0)
#         r = a + (b * 2)
#         sorted_scoville.append(r)
#         sorted_scoville.sort()
#         answer += 1

#     return answer


# 3차 시도 - heapq 모듈 사용 → 성공
import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)  # 스코빌 지수를 최소 힙으로 변환

    check = -1
    while scoville[0] < K:
        if len(scoville) < 2:
            return check if check < 0 else answer

        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        r = a + (b * 2)
        if r >= K:
            check += 1
        heapq.heappush(scoville, r)  # 새로운 스코빌 지수를 힙에 추가
        answer += 1
        print(scoville)

    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))  # 2
# print(solution([1, 1, 1], 10))  # -1
