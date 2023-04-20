def solution(brown, yellow):
    total = brown + yellow

    rst = []
    for i in range(total, 0, -1):
        if total % i == 0:
            rst.append(i)

    rst_r = sorted(rst)

    answer = []
    for i, v in enumerate(rst):
        if (v-2) * (rst_r[i]-2) == yellow: # yellow 값을 검증하여야 함
            answer = [v, rst_r[i]]
            break
    
    return answer

print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
print(solution(18, 6)) #[8, 3]