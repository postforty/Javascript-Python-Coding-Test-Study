# https://school.programmers.co.kr/learn/courses/30/lessons/133499?language=python3
# 딕셔너리 이용 - 성공
# def solution(babbling):
#     answer = 0

#     str_dict = {"a": "aya", "y": "ye", "w": "woo", "m": "ma"}

#     for str in babbling:
#         i = ""
#         while True:
#             if len(str) != 0:
#                 if i == str[0]:
#                     break
#                 i = str[0]
#             else:
#                 answer += 1
#                 break

#             if i in str_dict:
#                 if str[: len(str_dict[i])] == str_dict[i]:
#                     str = str[len(str_dict[i]) :]
#                     continue
#                 else:
#                     break

#     return answer


# 문자열 replace 메소드 이용 - 성공
def solution(babbling):
    answer = 0

    for str in babbling:
        if "ayaaya" in str or "yeye" in str or "woowoo" in str or "mama" in str:
            continue
        # wayaoo와 같은 경우 걸러내기 위해 "_" 이용함
        if not (
            str.replace("aya", "_")
            .replace("ye", "_")
            .replace("woo", "_")
            .replace("ma", "_")
            .replace("_", "")
        ):
            answer += 1
    return answer


# print(solution(["aya", "yee", "u", "maa"]))  # 1
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))  # 2
