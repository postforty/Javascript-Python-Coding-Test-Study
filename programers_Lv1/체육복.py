def solution(n, lost, reserve):
    answer = 0

    count = n - len(lost)
    chance = len(reserve)

    for i in lost:
        for j in reserve:
            if j-1 == i and chance:
                count += 1
                chance -= 1
                break
            elif j+1 == i and chance:
                count += 1
                chance -= 1
                break

    answer = count 

    return answer

print(solution(5, [2,4], [1,3,5]))
print(solution(5, [2,4], [3]))
print(solution(3, [3], [1]))