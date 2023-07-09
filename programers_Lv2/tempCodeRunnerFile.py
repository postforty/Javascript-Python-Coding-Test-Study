prime(n):
    #     if n < 2:  # 2 미만의 수는 소수가 아님
    #         return False
    #     for i in range(2, int(n**0.5) + 1):
    #         if n % i == 0:  # 약수가 존재하면 소수가 아님
    #             return False
    #     return True

    # def count_primes_in_string(s):
    #     count = 0

    #     for i in range(len(s)):
    #         for j in range(i + 1, len(s) + 1):
    #             number = int(s[i:j])
    #             if is_prime(number):
    #                 count += 1

    #     return count

    # return count_pr