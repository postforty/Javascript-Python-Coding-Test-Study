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
result += n - 1

print(result)
