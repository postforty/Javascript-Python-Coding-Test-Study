def solution(n):
    answer = [0, 1]

    if n == 0:
        return 0
    if n == 1:
        return 1
        
    for i in range(n-1):
        temp = (answer[0] + answer[1]) % 1234567
        answer[0] = answer[1]
        answer[1] = temp

    return answer[1]

print(solution(100))