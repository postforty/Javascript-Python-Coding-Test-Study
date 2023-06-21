# https://school.programmers.co.kr/learn/courses/30/lessons/67256
def solution(numbers, hand):
    answer = ''
    l = [1, 4, 7, 10]
    m = [2, 5, 8, 0]
    r = [3, 6, 9, 12]
    
    current_l = 10
    current_r = 12

    for i in numbers:
        if i in l:
            answer += 'L'
            current_l = i
        elif i in r:
            answer += 'R'
            current_r = i

    return answer

# print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
# "13458214595"
# "LRLLLRLLRRL"

print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
# 70828315762
# LRLLRRLLLRR