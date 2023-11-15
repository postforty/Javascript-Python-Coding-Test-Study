# https://school.programmers.co.kr/learn/courses/30/lessons/70128?language=python3
def solution(a, b):
    answer = 0

    # for i, v in enumerate(a):
    #     answer += v * b[i]

    # return answer
    
    for num_a, num_b in zip(a, b):
        answer += num_a * num_b
        
    return answer

print(solution([1,2,3,4], [-3,-1,0,2]))