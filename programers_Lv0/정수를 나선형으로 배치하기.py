# https://school.programmers.co.kr/learn/courses/30/lessons/181832
def solution(n):
    answer = [[0 for j in range(n)] for i in range(n)]

    def make_outer(arr, st, length, num):
        last = st+length-1 # 사각형 : (st,st)~(last,last)
        for c in range(st, last + 1): # 해당 최외각 사각형에서 첫째 행을 처리 -> (st,st)~(st,last)까지 작업
            arr[st][c] = num
            num += 1
        for r in range(st + 1, last + 1): # 해당 최외각 사각형에서 마지막 열을 처리 : (st,last)은 이미 차있음 -> (st+1,l)~(last,last)까지 작업
            arr[r][last] = num
            num += 1
        for c in range(last - 1, st - 1,-1): # 해당 최외각 사각형에서 마지막 행을 처리 : (last,last)은 이미 차있음 -> (last,last-1)~(last,st)까지 작업
            arr[last][c] = num
            num += 1
        for r in range(last - 1, st, -1): # 해당 최외각 사각형에서 첫번째 열을 처리 : (last,st), (st,st)은 이미 차있음 -> (last-1,st)~(st+1,st)까지 작업
            arr[r][st] = num
            num += 1
        return num

    j = n
    num = 1
    for i in range(n//2 if n % 2 == 0 else n//2 + 1):
        num = make_outer(answer, i, j, num)
        j -= 2

    return answer

print(solution(4))
