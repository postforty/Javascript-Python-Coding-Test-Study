# https://school.programmers.co.kr/learn/courses/30/lessons/12940?language=python3
def solution(n, m):
    answer = []

    def gcd_func(a, b):
        return b if a % b == 0 else gcd_func(b, a % b)

    # 최소공배수 = 두 자연수의 곱 / 최대공약수
    gcd = gcd_func(n, m)
    lcm = int(n * m / gcd)

    return [gcd, lcm]


print(solution(3, 12))
