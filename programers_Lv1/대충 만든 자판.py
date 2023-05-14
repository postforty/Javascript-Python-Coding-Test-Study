def solution(keymap, targets):
    t0, t1 = targets
    k0, k1 = keymap

    def func(target):
        cnt = 0
        for i in target:
            temp = [k0.find(i) + 1, k1.find(i) + 1]
            cnt += max(temp) if 0 in temp else min(temp)
        return cnt

    return [func(t0), func(t1)]


print(solution(["ABACD", "BCEFD"], ["ABCD", "AABB"]))  # [9, 4]
print(solution(["AA"], ["B"]))  # [9, 4]
