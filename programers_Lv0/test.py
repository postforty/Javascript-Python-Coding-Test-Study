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

    if temp_list[0][1] == 3:
        return (10 * temp_list[0][0] + temp_list[1][0]) ** 2

# print(solution(2, 2, 2, 2))
print(solution(4, 1, 4, 4))
