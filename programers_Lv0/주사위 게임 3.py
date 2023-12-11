def solution(a, b, c, d):
    if a == b == c == d:
        return 1111 * a

    temp_dict = {}
    for n in [a, b, c, d]:
        if n in temp_dict:
            temp_dict[n] += 1
        else:
            temp_dict[n] = 1

    temp_list = list(zip(temp_dict.keys(), temp_dict.values()))
    temp_list.sort(key=lambda x: x[1], reverse=True)

    if len(temp_dict) == 2:
        if temp_list[0][1] == 3:
            return (10 * temp_list[0][0] + temp_list[1][0]) ** 2

        if temp_list[0][1] == 2:
            return (temp_list[0][0] + temp_list[1][0]) * abs(temp_list[0][0] - temp_list[1][0])

    print(temp_list)
    if len(temp_dict) == 3:
        return (temp_list[1][0] * temp_list[2][0])

    return min(a, b, c, d)

# print(solution(2, 2, 2, 2))
# print(solution(4, 1, 4, 4))
# print(solution(6, 3, 3, 6))
# print(solution(2, 5, 2, 6))
print(solution(6, 4, 2, 5))
