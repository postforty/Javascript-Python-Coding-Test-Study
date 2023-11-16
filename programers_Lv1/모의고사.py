# https://school.programmers.co.kr/learn/courses/30/lessons/42840?language=python3
def solution(answers):
    students = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]

    students_pattern_len = []
    for lst in students:
        students_pattern_len.append(len(lst))
    
    answers_len = len(answers)

    for i, v in enumerate(students_pattern_len):
        if answers_len > v:
            students[i] = students[i] * (answers_len // students_pattern_len[i] if answers_len % students_pattern_len[i] == 0 else answers_len // students_pattern_len[i] + 1)
    
    count_list = [0, 0, 0]
    for i, v in enumerate(answers):
        for j in range(len(count_list)):
            if students[j][i] == v:
                count_list[j] += 1
        
    max_score = max(count_list)
    return list(map(lambda x: x+1, filter(lambda x: count_list[x] == max_score, range(len(count_list)))))

# print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))