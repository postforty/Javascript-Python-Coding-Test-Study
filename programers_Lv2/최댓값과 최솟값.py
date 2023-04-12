def solution(s):
    answer = ''

    lst = list(map(int, s.split()))

    min_rst = min(lst)
    max_rst = max(lst)

    answer = f'{min_rst} {max_rst}'

    return answer

print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))