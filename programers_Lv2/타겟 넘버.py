# https://school.programmers.co.kr/learn/courses/30/lessons/43165
def solution(numbers, target):
    answer = 0
    sum_numbers = sum(numbers)

    def get_sublists(arr):
        sublists = []

        def backtrack(start, curr):
            sublists.append(tuple(curr))

            for i in range(start, len(arr)):
                curr.append(arr[i])
                backtrack(i + 1, curr)
                curr.pop()

        backtrack(0, [])
        return sublists

    temp_lst = get_sublists(numbers)

    for t in temp_lst:
        if sum_numbers - (sum(t) * 2) == target:
            answer += 1

    return answer


print(solution([1, 1, 1, 1, 1], 3))  # 5
print(solution([4, 1, 2, 1], 4))  # 2
