# https://school.programmers.co.kr/learn/courses/30/lessons/250121
def solution(data, ext, val_ext, sort_by):
    answer = []

    column = ["code", "date", "maximum", "remain"]

    ext_idx = column.index(ext)
    sort_by_idx = column.index(sort_by)

    for i in data:
        if i[ext_idx] < val_ext:
            answer.append(i)

    answer.sort(key=lambda x: x[sort_by_idx])

    return answer
    # return sorted(answer, key=lambda x: x[sort_by_idx])


print(
    solution(
        [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]],
        "date",
        20300501,
        "remain",
    )
)
