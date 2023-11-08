n, k = 10, 2

result = 0

while True:
    rest = n % k
    target = n - rest
    result += rest
    n = target
    if n < k:
        break
    n //= k
    result += 1
result += n - 1  # 1이 될때까지 이므로 -1을 적용함

print(result)
