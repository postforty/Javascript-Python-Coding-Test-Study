def solution(park, routes):
    answer = []
    start = []
    x_point = []
    y_len = len(park)
    x_len = len(park[0])

    for i, v in enumerate(park):
        for j, s in enumerate(v):
            if s == 'S':
                start = [i, j]
            if s == 'X':
                x_point.append([i, j])
    
    # ! 장애물 좌표와 동일한 위치 뿐만 아니라 이동 중에 만난 장애물에 대한 처리도 고려해야 함
    for i in routes:
        a, b = i.split()
        b = int(b)
        # 가로 - 우
        if a == "E" and start[1] + b < x_len:
            temp = start[:]
            for j in range(b):
                temp[1] += 1
                if temp not in x_point:
                    start[1] += 1
                else:
                    break
        # 가로 - 좌
        if a == "W" and start[1] - b >= 0:
            temp = start[:]
            for j in range(b):
                temp[1] -= 1
                if temp not in x_point:
                    start[1] -= 1
                else:
                    break
        # 세로 - 상
        if a == "N" and start[0] - b >= 0:
            temp = start[:]
            for j in range(b):
                temp[0] -= 1
                if temp not in x_point:
                    start[0] -= 1
                else:
                    break
        # 세로 - 하
        if a == "S" and start[0] + b < y_len:
            temp = start[:]
            for j in range(b):
                temp[0] += 1
                # ! 진행 중에 장해물을 만나면 롤백 시켜야 함
                if temp not in x_point:
                    start[0] += 1
                else:
                    break
            print(start)
            
    
    return start

# W - 좌, E - 우, N - 상, S - 하 
# print(solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"])) # [2,1]
# print(solution(["SOO","OXX","OOO"], ["E 2","S 2","W 1"])) # [0,1]
print(solution(["OSO","OOO","OXO","OOO"], ["E 2","S 3","W 1"])) # [0,0]