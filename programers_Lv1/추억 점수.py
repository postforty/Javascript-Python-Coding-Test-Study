# https://school.programmers.co.kr/learn/courses/30/lessons/176963?language=python3
def solution1(name, yearning, photo):
    answer = []
    score_board = {}
    for id, key in enumerate(name):
        score_board[key] = yearning[id]
    for i in photo:
        score = 0
        for j in i:
            try:
                score += score_board[j]
            except:
                pass

        answer.append(score)

    return answer

print(solution1(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]])) # [19, 15, 6]

def solution2(name, yearning, photo):
    answer = []
    score_board = dict(zip(name, yearning))
    for i in photo:
        score = 0
        for j in i:
            if j in score_board:
                score += score_board[j]

        answer.append(score)

    return answer

print(solution2(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]])) # [19, 15, 6]

def solution3(name, yearning, photo):
    return [sum(yearning[name.index(j)] for j in i if j in name) for i in photo]

print(solution3(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]])) # [19, 15, 6]