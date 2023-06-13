import re
def solution(s):
    s_split = s.split(',')
    s_nums = list([int(re.sub('[^0-9]+','', n)) for n in s_split])
    s_dict = {}
    for v in s_nums:
        try:
            s_dict[v] += 1
        except:
            s_dict[v] = 1
    answer = [n[0] for n in sorted(s_dict.items(), key = lambda x: x[1], reverse=True)]
    return answer

# print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")) # [2, 1, 3, 4]
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")) # [3, 2, 4, 1]
