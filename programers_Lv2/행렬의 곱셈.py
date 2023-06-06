def solution(arr1, arr2):
    answer = []

    new_arr2 = []
    for i in range(len(arr2[0])):
        temp = []
        for v in arr2:
            temp.append(v[i])
        new_arr2.append(temp)

    def func(arr1, arr2):
        rst = 0
        for i in range(len(arr1)):
            rst += arr1[i] * arr2[i]
        return rst

    for v in arr1:
        temp = []
        for w in new_arr2:
            temp.append(func(v, w))
        answer.append(temp)

    return answer


print(
    solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]])
)  # [[15, 15], [15, 15], [15, 15]]
