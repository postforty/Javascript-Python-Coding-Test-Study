# https://school.programmers.co.kr/learn/courses/30/lessons/250125?language=python3
def solution(board, h, w):
    count = 0

    n = len(board)

    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]

    for i in range(4):
        h_check = h + dh[i]
        w_check = w + dw[i]
        if h_check >= 0 and h_check < n and w_check >= 0 and w_check < n:
            if board[h][w] == board[h_check][w_check]:
                count += 1

    return count


print(
    solution(
        [
            ["blue", "red", "orange", "red"],
            ["red", "red", "blue", "orange"],
            ["blue", "orange", "red", "red"],
            ["orange", "orange", "red", "blue"],
        ],
        1,  # h
        1,  # w
    )
)

# print(
#     solution(
#         [
#             ["yellow", "green", "blue"],
#             ["blue", "green", "yellow"],
#             ["yellow", "blue", "blue"],
#         ],
#         0,
#         1,
#     )
# )
