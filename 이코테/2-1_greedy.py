# greedy
# n이 1이 될 때까지 k로-나누어 떨어질 경우-나누거나-나누어 떨어지지 않을 경우-1을 뺌

n, k = 10, 2

result = 0

while True:
    # target = (n // k) * k
    target = n - n % k
    result += n - target
    n = target
    if n < k:
        break
    result += 1
    n //= k

result += n - 1  # 1이 될때까지 이므로 -1을 적용함
print(result)

# https://www.youtube.com/watch?v=2zjoKjt97vQ&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=2
# 18:56부터
