def solution(n):
    ans = 1
    div_n = n
    
    while div_n > 1:
        if div_n % 2 != 0:
            div_n = div_n // 2
            ans += 1
        else:
            div_n = div_n / 2

    return ans

print(solution(5)) # 2
print(solution(6)) # 2
print(solution(5000)) # 5