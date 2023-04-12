def solution(A,B):
    answer = 0

    A.sort()
    B.sort(reverse=True)

    for i in range(len(A)):
        answer += A[i] * B[i]

    return answer

    # 1: min, max, index 사용시 시간 초과 발생
    # def min_func(lst):
    #     return lst.pop(lst.index(min(lst)))
    # def max_func(lst):
    #     return lst.pop(lst.index(max(lst)))
    # while a_lst:
    #     answer += min_func(a_lst) * max_func(b_lst)

    # 2: 재귀 사용시 런타임 에러 발생
    # return mul + solution(a_lst, b_lst) if a_lst else mul 

print(solution([1,2], [3,4]))
print(solution([1, 4, 2], [5, 4, 4]))