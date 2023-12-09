# https://school.programmers.co.kr/learn/courses/30/lessons/12930#qna
def solution(s):
    s_list = s.split(' ')
    answer = ''
    for word in s_list:
        for i, v in enumerate(word):
            if i % 2 == 0:
                answer += v.upper()
            else:
                answer += v.lower()
        answer += ' '

    return answer[:-1]

print(solution("try hello world"))
print(solution("a  b  c"))
