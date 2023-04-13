def solution(n):
    answer = 0
    for i in range(1, n+1):
        temp = 0
        for j in range(i, n+1):
            if temp < n+1:
                temp += j
            if temp == n:
                answer += 1
            if temp > n:
                break # 효율성 테스트 통과 위해

    return answer

print(solution(15))