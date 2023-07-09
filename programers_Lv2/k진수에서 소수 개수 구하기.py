# https://school.programmers.co.kr/learn/courses/30/lessons/92335
def solution(n, q):
    rev_base = ""

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    rev_base = rev_base[::-1]
    # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력

    temp_lst = rev_base.split("0")
    count = 0

    # 소수인지 판별하는 함수
    def is_prime(num):
        for i in range(
            3, int(num**0.5) + 1
        ):  # num만 작성한 경우 시간 초과 => int(num**0.5) + 1
            if num % i == 0:
                return 0
        return 1

    for i in temp_lst:
        num = int(i) if len(i) != 0 else 0
        if num < 2:
            continue
        if num == 2:
            count += 1
        else:
            count += is_prime(num)
    return count


print(solution(437674, 3))
