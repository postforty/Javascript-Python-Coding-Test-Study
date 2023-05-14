def solution(keymap, targets):
    def func(k, t):
        result = []
        for i in t:
            result.append(k.find(i) + 1 if k.find(i) >= 0 else k.find(i))
        return result

    return func(keymap[0], targets[0])


# print(solution(["ABACD", "BCEFD"], ["ABCD", "AABB"]))  # [9, 4]
print(solution(["AA"], ["B"]))  # [-1]
