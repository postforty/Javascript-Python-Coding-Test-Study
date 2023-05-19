def solution(n):
    ans = 1
    current = 1
    
    limit = n

    while current < n:
        temp = current
        if temp < limit:
            temp += current
            if temp > limit:
                temp = current
                temp += 1
                ans += 1
                current = temp
                print(temp)

            else:
                current = temp
    return ans

# print(solution(5)) # 2
print(solution(6)) # 2
# print(solution(5000)) # 5