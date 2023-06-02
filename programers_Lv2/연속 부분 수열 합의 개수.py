import itertools

def solution(elements):
    answer = set(elements)

    for i in range(2, len(elements)+1):
        for _ in range(len(elements)):
            answer.add(sum(elements[:i]))
            elements = elements[1:]+elements[:1]
    
    return len(answer)

print(solution([7,9,1,1,4])) # 18