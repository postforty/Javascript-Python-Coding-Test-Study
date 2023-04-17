def solution(park, routes):
    answer = []
    S = []
    X = []

    for i, v in enumerate(park):
        for j, v in enumerate(v):
            if v == 'S':
                S = [i, j]
            if v == 'X':
                X.append([i, j])
    
    move = S[:]
    for i in routes:
        coord = i.split()
        coord[1] = int(coord[1])

        rollback = False
        temp = move[:]
        if coord[0] == 'W':
            for _ in range(coord[1]):
                move[1] = move[1] - 1
                if move in X or move[1] < 0:
                    rollback = True
        if coord[0] == 'E':
            for _ in range(coord[1]):
                move[1] = move[1] + 1
                if move in X or move[1] >= len(i):
                    rollback = True
        if coord[0] == 'N':
            for _ in range(coord[1]):
                move[0] = move[0] - 1
                if move in X or move[0] < 0:
                    rollback = True
        if coord[0] == 'S':
            for _ in range(coord[1]):
                move[0] = move[0] + 1
                if move in X or move[0] >= len(park):
                    rollback = True

        if rollback:
            move = temp[:]

    answer = move[:]

    return answer

# W - 좌, E - 우, N - 상, S - 하 
# print(solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"])) # [2,1]
# print(solution(["SOO","OXX","OOO"], ["E 2","S 2","W 1"])) # [0,1]
# print(solution(["OSO","OOO","OXO","OOO"], ["E 2","S 3","W 1"])) # [0,0]
print(solution(["OO","OS","OO"], ["E 2","S 2","W 1"])) # [2,1]
