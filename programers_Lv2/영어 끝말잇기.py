def solution(n, words):
    answer = []
    lst_1 = words[:-1]
    lst_2 = words[1:]

    print(lst_1)
    print(lst_2)
    cnt = 1
    for i, v in enumerate(lst_1):
        if v[-1] != lst_2[i][0] or lst_2[i] in lst_1[:i]:
            player = n if (i + 1) % n == 0 else (i + 1) % n
            break
        else:
            if ((i+1) % n == 0):
                cnt += 1

    print(cnt, player)

    return answer

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))