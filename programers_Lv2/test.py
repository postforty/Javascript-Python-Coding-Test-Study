# https://school.programmers.co.kr/learn/courses/30/lessons/42626?language=python3
# 1차 시도 → 테스트케이스 1~16 실패, 효율성 테스트 실패
def solution(scoville, K):
    answer = 0
    scoville.sort()
    idx = 0
    for i, v in enumerate(scoville):
        if v >= K:
            idx = i
            break
    new_scoville = scoville[:idx+1]

    while len(new_scoville) > 1:
        result = new_scoville[0] + (new_scoville[1]*2)
        if result < K:
            new_scoville = new_scoville[2:] + [result]
            new_scoville.sort()
            answer += 1
        else:
            new_scoville = new_scoville[2:]
            answer += 1

    return answer

print(solution([1, 2, 3, 9, 10, 12], 7)) # 2