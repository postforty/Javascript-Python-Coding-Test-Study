def solution(n, lost, reserve):
    answer = 0

    count = n - len(lost)
    solted_lost = sorted(lost)
    solted_lost_remove = sorted(lost) # 순회 중인 리스트의 요소를 제거하면 안되기 때문에 새로운 리스트 생성
    solted_reserve = sorted(reserve)

    # 여벌을 가지고 있는데 잃어 버린 경우에 대한 처리를 먼저해야 함.
    for i in solted_lost:
        if i in solted_reserve:
            solted_lost_remove.remove(i)
            solted_reserve.remove(i)
            count += 1
    
    for i in solted_lost_remove:
        if i-1 in solted_reserve:
            solted_reserve.remove(i-1)
            count += 1
            continue
        if i+1 in solted_reserve:
            solted_reserve.remove(i+1)
            count += 1

    answer = count

    return answer

print(solution(5, [2,4], [1,3,5])) # 5
print(solution(5, [2,4], [3])) # 4
print(solution(3, [3], [1])) # 2
print(solution(5, [4,2], [3,5])) # 5
print(solution(4, [2,3], [3,4])) # 3