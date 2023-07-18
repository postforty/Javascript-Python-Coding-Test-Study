# https://school.programmers.co.kr/learn/courses/30/lessons/42626
import string


def solution(msg):
    answer = []
    alpa_list = {v: i + 1 for i, v in enumerate(list(string.ascii_uppercase))}
    new_num = 27

    new_msg = msg
    temp_str = ""
    print(new_msg[0])
    while True:
        if new_msg == "":
            break
        if new_msg[0] in alpa_list:
            temp_str += new_msg[0]
            new_msg = new_msg[1:]
            continue
        if temp_str not in alpa_list:
            alpa_list[temp_str] = new_num
            temp_str = ""
            new_num += 1
            continue
        else:
            answer.append(alpa_list[temp_str])

    return answer


print(solution("KAKAO"))  # [11, 1, 27, 15]
