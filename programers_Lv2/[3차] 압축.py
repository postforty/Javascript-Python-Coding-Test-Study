# https://school.programmers.co.kr/learn/courses/30/lessons/17684
import string

def solution(msg):
    answer = []
    new_value = 27
    alpa_dict = {v: i+1 for i, v in enumerate(string.ascii_uppercase)}

    new_msg = msg
    temp_str = ''
    while True:
        try:
            temp_str += new_msg[0]
            if temp_str in alpa_dict:
                new_msg = new_msg[1:]
                continue
            else:
                alpa_dict[temp_str] = new_value
                new_value += 1
                answer.append(alpa_dict[temp_str[:-1]])
                temp_str = ''
        except:
            answer.append(alpa_dict[temp_str])
            return answer
        
print(solution("KAKAO"))  # [11, 1, 27, 15]
