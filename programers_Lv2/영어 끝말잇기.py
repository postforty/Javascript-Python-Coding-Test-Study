def solution(n, words):
    answer = []
    lst_1 = words[:]
    lst_2 = words[1:]

    lst_player_num = []
    lst_round = []
    round = 1
    for i in range(1, len(words) + 1):

        if i % n == 0:
            lst_player_num.append(n)
            lst_round.append(round)
            cnt += 1
        else:
            lst_player_num.append(i % n)
            lst_round.append(round)


    # print(lst_1)
    # print(lst_2)
    # print(lst_player_num)
    # print(lst_round)

    for i, v in enumerate(lst_1):
        try:
            if v[-1] != lst_2[i][0]:
                answer = [lst_player_num[i+1], lst_round[i+1]]
                break
            if lst_2[i] in lst_1[:i+1]:
                print("!!!",lst_1[:i+1])
                answer = [lst_player_num[i+1], lst_round[i+1]]
                break
        except:
            answer = [0, 0]
            break

    return answer # [player, round]

print(solution(3, ['aa', 'ab', 'bc', 'ca', 'aaa', 'abb', 'bc', 'ca', 'aa'])) # [1, 3] / 17, 19에서 에러 발생. 해결하기 위해 만든 예제. 리스트 내에 여러개의 중복 요소를 추가하였음
print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])) # [3, 3]
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"])) # [0, 0]
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"])) # [1, 3]