def solution(d, budget):
    answer = 0
    sum = 0

    d.sort()

    for i in d:
        sum += i
        if budget < sum:
            break
        answer += 1

    return answer

print(solution([1,3,2,5,4], 9))
print(solution(	[2, 2, 3, 3], 10))