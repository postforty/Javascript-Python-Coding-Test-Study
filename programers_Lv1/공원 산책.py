def solution(park, routes):
    answer = []
    x_point = []
    y_len = len(park)
    x_len = len(park[0])

    for i, v in enumerate(park):
        for j, s in enumerate(v):
            if s == 'S':
                answer = [i, j]
            if s == 'X':
                x_point.append([i, j])
    
    for i in routes:
        a, b = i.split()
        b = int(b)
        # 가로 - 우
        if a == "E" and answer[1] + b < x_len:
            temp = answer[:]
            rollback = False
            for j in range(b):
                temp[1] += 1
                if temp in x_point:
                    rollback = True
            if rollback == False:
                answer = temp
        # 가로 - 좌
        if a == "W" and answer[1] - b >= 0:
            temp = answer[:]
            rollback = False
            for j in range(b):
                temp[1] -= 1
                if temp in x_point:
                    rollback = True
            if rollback == False:
                answer = temp
        # 세로 - 상
        if a == "N" and answer[0] - b >= 0:
            temp = answer[:]
            for j in range(b):
                temp[0] -= 1
                if temp in x_point:
                    rollback = True
            if rollback == False:
                answer = temp
        # 세로 - 하
        if a == "S" and answer[0] + b < y_len:
            temp = answer[:]
            rollback = False
            for j in range(b):
                temp[0] += 1
                if temp in x_point:
                    rollback = True
            if rollback == False:
                answer = temp
    
    return answer

# W - 좌, E - 우, N - 상, S - 하 
print(solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"])) # [2,1]
print(solution(["SOO","OXX","OOO"], ["E 2","S 2","W 1"])) # [0,1]
print(solution(["OSO","OOO","OXO","OOO"], ["E 2","S 3","W 1"])) # [0,0]