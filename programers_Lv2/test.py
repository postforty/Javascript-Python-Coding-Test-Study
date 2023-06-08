def solution(clothes):
    answer = len(clothes)
    dict = {}
    for v in clothes:
        dict[v[1]] = []
    for v in clothes:
        dict[v[1]].append(v[0])
    dict_lst = list(dict.values())
    print(dict_lst)

    add = 0
    num_lst = [1]
    for i in range(len(dict_lst) - 1):
        temp = 0
        for j, v in enumerate(dict_lst[i]):
            temp += num_lst[i] * 1
        num_lst.append(temp)
    for i in range(1, len(num_lst)):
        for _ in dict_lst[i]:
            add += num_lst[i]
    return answer + add


# print(
#     solution(
#         [
#             ["yellow_hat", "headgear"],
#             ["blue_sunglasses", "eyewear"],
#             ["green_turban", "headgear"],
#         ]
#     )
# )  # 5
# print(
#     solution(
#         [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
#     )
# )  # 3

print(
    solution(
        [
            ["a", "headgear"],
            ["b", "headgear"],
            ["c", "eyewear"],
            ["d", "eyewear"],
            ["e", "face"],
            ["f", "face"],
        ]
    )
)  # 26
