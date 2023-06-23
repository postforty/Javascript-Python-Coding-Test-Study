# https://school.programmers.co.kr/learn/courses/30/lessons/87946
import itertools
def solution(k, dungeons):
    answer = 0
    nPr = itertools.permutations(dungeons, len(dungeons))
    for i in nPr:
        cur_k = k
        cnt = 0
        for j in i:
            if cur_k >= j[0]:
                cur_k -= j[1]
                cnt += 1
        if cnt > answer:
            answer = cnt
    return answer

print(solution(80, [[80,20],[50,40],[30,10]])) # 3
