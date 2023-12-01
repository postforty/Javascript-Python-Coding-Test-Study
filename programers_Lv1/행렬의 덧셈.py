# https://school.programmers.co.kr/learn/courses/30/lessons/12950
def solution(arr1, arr2):
    answer = []
    for v in zip(arr1, arr2):
        temp_list = []
        for w in zip(v[0], v[1]):
            temp_list.append(sum(w))
        answer.append(temp_list)
    return answer


print(solution([[1, 2], [2, 3]], [[3, 4], [5, 6]]))
