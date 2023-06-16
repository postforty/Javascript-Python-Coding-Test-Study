# https://school.programmers.co.kr/learn/courses/30/lessons/131127
def solution(want, number, discount):
    answer = 0

    for i in range(len(discount)-9):
        temp_list = discount[i:i+10]
        temp_cnt = 0
        for j, v in enumerate(want):
            count = temp_list.count(v)
            if count != number[j]:
                break
            temp_cnt += 1
            print(temp_list)
        answer += 1 if temp_cnt == len(want) else 0
    return answer

print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"])) # 3
# print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "banana"])) # 3