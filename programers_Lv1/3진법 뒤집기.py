# https://school.programmers.co.kr/learn/courses/30/lessons/68935#qna
def solution(n):
    answer = ''
    while True:
        if n < 3:
            answer += str(n)
            break
        answer += str(n % 3)
        n = n // 3
    
    return int(answer, 3)

print(solution(45))
# print(solution(1)) # if 조건문을 while문 마지막에 두었을때 결과가 1이 아닌 3이 나온다. 따라서 조건문을 위로 올렸다.