from pprint import pprint as pp
def solution(board):
    answer = 0

    dic = {}

    for idx, lst in enumerate(board):
        dic[idx] = lst
    
    for i, l in enumerate(board):
        for j, v in enumerate(l):
            if v == 1 and not j:
                try:
                    dic[i-1][j] = 2 if dic[i-1][j] != 1 else dic[i-1][j]
                except:
                    pass
                try:
                    dic[i-1][j+1] = 2 if dic[i-1][j+1] != 1 else dic[i-1][j+1]
                except:
                    pass
                try:
                    dic[i][j+1] = 2 if dic[i][j+1] != 1 else dic[i][j+1]
                except:
                    pass
                try:
                    dic[i+1][j] = 2 if dic[i+1][j] != 1 else dic[i+1][j]
                except:
                    pass
                try:
                    dic[i+1][j+1] = 2 if dic[i+1][j+1] != 1 else dic[i+1][j+1]
                except:
                    pass
            elif v == 1:
                try:
                    dic[i-1][j-1] = 2 if dic[i-1][j-1] != 1 else dic[i-1][j-1]
                except:
                    pass
                try:
                    dic[i-1][j] = 2 if dic[i-1][j] != 1 else dic[i-1][j]
                except:
                    pass
                try:
                    dic[i-1][j+1] = 2 if dic[i-1][j+1] != 1 else dic[i-1][j+1]
                except:
                    pass
                try:
                    dic[i][j-1] = 2 if dic[i][j-1] != 1 else dic[i][j-1]
                except:
                    pass
                try:
                    dic[i][j+1] = 2 if dic[i][j+1] != 1 else dic[i][j+1]
                except:
                    pass
                try:
                    dic[i+1][j-1] = 2 if dic[i+1][j-1] != 1 else dic[i+1][j-1]
                except:
                    pass
                try:
                    dic[i+1][j] = 2 if dic[i+1][j] != 1 else dic[i+1][j]
                except:
                    pass
                try:
                    dic[i+1][j+1] = 2 if dic[i+1][j+1] != 1 else dic[i+1][j+1]
                except:
                    pass
    
    pp(dic)

    for val  in dic.values():
        answer += val.count(0)

    return answer


board = [[0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
# board = [
#     [0, 0, 0, 0, 0], 
#     [0, 0, 0, 0, 0], 
#     [0, 0, 0, 0, 0], 
#     [0, 0, 1, 0, 0], 
#     [0, 0, 0, 0, 0]]
# board = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]

pp(solution(board))