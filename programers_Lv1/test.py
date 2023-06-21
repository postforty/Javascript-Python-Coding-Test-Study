# https://school.programmers.co.kr/learn/courses/30/lessons/67256
def solution(numbers, hand):
    answer = ""
    l = [1, 4, 7, 10]
    m = [2, 5, 8, 0]
    r = [3, 6, 9, 12]

    cur_l = 10
    cur_r = 12

    def func(num, cur, arr):
        m_idx = m.index(num)
        arr_idx = arr.index(cur)
        if m[0] == arr[0]:
            if m_idx < arr_idx:
                return len(m[m_idx:arr_idx])
            elif m_idx == arr_idx:
                return 0
            else:
                return len(m[arr_idx:m_idx])
        else:
            if m_idx < arr_idx:
                return len(m[m_idx:arr_idx]) + 1
            elif m_idx == arr_idx:
                return 1
            else:
                return len(m[arr_idx:m_idx]) + 1

    for num in numbers:
        if num in l:
            answer += "L"
            cur_l = num
        elif num in r:
            answer += "R"
            cur_r = num
        else:
            if cur_l in m:
                temp_l = func(num, cur_l, m)
            if cur_r in m:
                temp_r = func(num, cur_r, m)
            if cur_l in l:
                temp_l = func(num, cur_l, l)
            if cur_r in r:
                temp_r = func(num, cur_r, r)
            if temp_l == temp_r:
                if hand == "left":
                    cur_l = temp_l
                    answer += "L"
                if hand == "right":
                    cur_r = temp_r
                    answer += "R"
            elif temp_l < temp_r:
                cur_l = temp_l
                answer += "L"
            else:
                cur_r = temp_r
                answer += "R"

    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
# "13458214595"
# "LRLLLRLLRRL"

# print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
# 70828315762
# LRLLRRLLLRR
