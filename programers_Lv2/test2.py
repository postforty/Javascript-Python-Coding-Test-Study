# https://school.programmers.co.kr/learn/courses/30/lessons/131128
def solution(X, Y):
    result_str = ''
    for i in X:
        target = Y.find(i)
        if target > -1:
            result_str += Y[target]
            Y = Y[:target] + Y[target+1:]
    
    if len(result_str) == 0:
        return "-1"
    
    answer = ''.join(list(map(str, sorted(map(int, list(result_str)), reverse=True))))

    return answer

print(solution("5525", "1255")) # "552"
print(solution("100", "2345")) # "-1"
print(solution("100", "203045")) # 	"0"