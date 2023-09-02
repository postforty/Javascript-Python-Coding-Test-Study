# https://school.programmers.co.kr/learn/courses/30/lessons/155652?language=python3

import string

# 1차 시도 - 런타임 에러
# def solution(s, skip, index):
#     answer = ""
#     s_list = list(string.ascii_lowercase)
#     for i in skip:
#         s_list.remove(i)

#     new_s = "".join(s_list)

#     for i in s:
#         idx = new_s.find(i) + index
#         if idx >= len(new_s):
#             idx = idx - len(new_s)
#         answer += new_s[idx]
#     return answer


# 2차 성공 - 나머지 연산 적용
def solution(s, skip, index):
    answer = ""

    s_list = [x for x in string.ascii_lowercase if x not in skip]
    s_list_length = len(s_list)

    for i in s:
        idx = s_list.index(i) + index
        if idx >= s_list_length:
            idx = idx % s_list_length
        answer += s_list[idx]
    return answer


print(solution("aukks", "wbqd", 5))  # "happy"
