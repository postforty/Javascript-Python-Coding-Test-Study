# https://school.programmers.co.kr/learn/courses/30/lessons/136798?language=python3
def solution(number, limit, power):
    answer = 0

    for n in range(1, number+1):
        count = 0
        for m in range(1, n+1):
            count += 1 if n % m == 0 else 0
            if count > limit:
                count = power
                break
        answer += count
    
    return answer

print(solution(10, 3, 2))  # 21
