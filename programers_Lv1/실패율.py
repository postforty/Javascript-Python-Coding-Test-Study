def solution(N, stages):
    answer = []

    count = len(stages)

    stageDict = {}

    for i in range(1, N+1):
        stageDict[i] = 0
    
    for i in stages:
        stageDict[(i)] += 1

    return stageDict

print(solution(4, [4, 4, 4, 4, 4]))