# https://school.programmers.co.kr/learn/courses/30/lessons/42577#qna
def solution(phone_book):
    set_phone_book = set([len(i) for i in phone_book])
    for i in set_phone_book:
        temp_list = [x[:i] for x in phone_book]
        if len(temp_list) != len(set(temp_list)):
            temp_dict = {}
            for j in temp_list:
                try:
                    temp_dict[j] += 1
                    if temp_dict[j] == 2 and j in phone_book:
                        return False
                except:
                    temp_dict[j] = 1

    return True


# 풀이:
# 1. phone_book의 요소를 순회시키고 해당 요소의 길이만큼 다른 요소를 슬라이싱하여 요소의 길이를 맞춘 새로운 리스트 생성
# 2. phone_book의 길이와 새롭게 생성된 리스트의 중복을 제거한 set의 길이가 다를 경우 앞자리가 중복 동일할 가능성이 있음(False의 가능성 있음)
# 3. 슬라이싱한 리스트(temp_list)의 요소 중 동일한 요소가 2개인 경우 False의 가능성이 있음
# 4. 동일한 요소가 2개인 경우 phone_book에 해당 요소가 있는지 체크, 있담면 False로 확정


print(solution(["119", "97674223", "1195524421"]))  # false
print(solution(["12", "123", "1235", "567", "88"]))  # false
print(solution(["123", "1005", "1006", "1007"]))  # true
