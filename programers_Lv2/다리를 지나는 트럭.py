
# https://school.programmers.co.kr/learn/courses/30/lessons/42583?language=python3
# 다리를 지나는 트럭

# 시간초과, 테스트 8번 실패

# from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    current_weight = 0

    while truck_weights or current_weight > 0:
        answer += 1
        current_weight -= bridge.pop(0)

        if truck_weights:
            if current_weight + truck_weights[0] <= weight:
                truck = truck_weights.pop(0)
                bridge.append(truck)
                current_weight += truck
            else:
                bridge.append(0)

    return answer


print(solution(2, 10, [7, 4, 5, 6]))  # 8
