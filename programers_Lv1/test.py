# https://school.programmers.co.kr/learn/courses/30/lessons/250137?language=python3
def solution(bandage, health, attacks):
    b1, b2, b3 = bandage

    attack_time = []
    damage = []
    for a, b in attacks:
        attack_time.append(a)
        damage.append(b)

    player_health = health
    bonus = 0
    for i in range(1, attack_time[-1] + 1):
        if i in attack_time:
            bonus = 0
            player_health -= damage[attack_time.index(i)]
            continue
        if player_health < health:
            bonus += 1
            player_health += b2
        if bonus == b1:
            bonus = 0
            player_health += b3
        if player_health > health:
            player_health = health

    return player_health if player_health > 0 else -1


print(solution([5, 1, 5], 30, [[2, 10], [9, 15], [10, 5], [11, 5]]))
