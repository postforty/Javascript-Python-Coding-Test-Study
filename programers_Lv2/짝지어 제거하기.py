def solution(s):
    rst = []

    rst.append(s[0])

    for c in s[1:]:
        if not rst:
            rst.append(c)
        elif rst[-1] != c:
            rst.append(c)
        elif rst[-1] == c:
            del(rst[-1])

    return (lambda x: 1 if not rst else 0)(rst)

print(solution('baabaa'))
print(solution('cdcd'))