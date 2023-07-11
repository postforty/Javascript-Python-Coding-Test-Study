# https://school.programmers.co.kr/learn/courses/30/lessons/178871
def solution(players, callings):
    called = {}
    for i in callings:
        try:
            called[i] -= 1
        except:
            idx = players.index(i)
            called[i] = idx
        print(called[i])
        # temp_players = players[:called[i]] + players[called[i]+1:]
        # temp_players = temp_players[:called[i]-1] + [i] + temp_players[called[i]-1:]
        # players = temp_players
    return players

print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"])) # ["mumu", "kai", "mine", "soe", "poe"]