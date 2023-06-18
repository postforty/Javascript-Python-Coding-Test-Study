def solution(priorities, location):
    answer = 0
    new_p = []
    for i, v in enumerate(priorities):
        new_p.append((v, i))
    value = new_p[location]

    while True:
        idx = priorities.index(max(priorities))
        temp = new_p[idx]
        priorities = priorities[idx + 1 :] + priorities[:idx]
        new_p = new_p[idx + 1 :] + new_p[:idx]

        answer += 1
        if value == temp:
            break

    return answer


# print(solution([2, 1, 3, 2], 2))  # 1
print(solution([1, 1, 9, 1, 1, 1], 0))  # 5
