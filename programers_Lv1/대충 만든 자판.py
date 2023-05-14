def solution(keymap, targets):
    def func(k, t):
        result = []
        for i in t:
            result.append(k.find(i) + 1 if k.find(i) >= 0 else k.find(i))
        return result

    t_lst = []
    for t in targets:
        k_lst = []
        for k in keymap:
            k_lst.append(func(k, t))
        print(k_lst)

    return


print(solution(["ABACD", "BCEFD"], ["ABCD", "AABB"]))  # [9, 4]
# print(solution(["AA"], ["B"]))  # [-1]
