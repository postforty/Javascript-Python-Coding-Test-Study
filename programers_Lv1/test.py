# https://school.programmers.co.kr/learn/courses/30/lessons/133499?language=python3
def solution(babbling):
    answer = 0

    str_dict = {'a': "aya", 'y': "ye", 'w': "woo", 'm': "ma"}

    str = babbling[3]

    while True:
        try:
            i = str[0]

            if i in str_dict:
                if str[:len(str_dict[i])] == str_dict[i]:
                    str = str[len(str_dict[i]):]
                    continue
                else:
                    break
        except:
            answer += 1
            break



    print(answer)

    return


# print(solution(["aya", "yee", "u", "maa"]))  # 1
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))  # 2
