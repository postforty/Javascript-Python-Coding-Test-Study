# https://school.programmers.co.kr/learn/courses/30/lessons/181881
def solution(arr):
    answer = 0
    old_arr = arr[:]
    new_arr = []

    while True:
        new_arr = []

        for n in old_arr:
            if n >= 50 and n % 2 == 0:
                new_arr.append(int(n / 2))
            elif n < 50 and n % 2 != 0:
                new_arr.append(n * 2 + 1)
            else:
                new_arr.append(n)

        if old_arr == new_arr:
            return answer

        old_arr = new_arr[:]

        answer += 1

print(solution([1, 2, 3, 100, 99, 98]))
