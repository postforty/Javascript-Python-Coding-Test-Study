def solution(s):
    char_list = list(s.lower())

    char_list[0] = char_list[0].upper()

    for i in range(len(char_list)):
        if char_list[i] != ' ' and char_list[i-1] == ' ':
            char_list[i] = char_list[i].upper()

    return ''.join(char_list)

print(solution("  a  3peoPle 3peoPle  unFollowed me    me unFollowed"))
print(solution('    aaaaa aaa aaaaaaa a aa a'))
print(solution(" 3people unFollowed me"))
print(solution("aaa a   aaa    "))
print(solution("for the last week"))