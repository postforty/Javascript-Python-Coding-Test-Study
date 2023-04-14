def solution(n):
    answer = 0
    n_cnt = bin(n).count('1') # bin(n)은 문자열을 반환

    while True:
        n += 1
        temp_cnt = bin(n).count('1')
        if temp_cnt == n_cnt:
            answer = n
            break
    return answer

print(solution(15))