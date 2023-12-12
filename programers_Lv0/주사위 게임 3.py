# https://school.programmers.co.kr/learn/courses/30/lessons/181916?language=python3
def solution(a, b, c, d):
    # 네 주사위에서 나온 숫자가 모두 p로 같다면 1111 × p점을 얻습니다.
    if a == b == c == d:
        return 1111 * a

    temp_dict = {}
    for n in [a, b, c, d]:
        if n in temp_dict:
            temp_dict[n] += 1
        else:
            temp_dict[n] = 1

    temp_list = list(zip(temp_dict.keys(), temp_dict.values()))
    temp_list.sort(key=lambda x: x[1], reverse=True)

    if len(temp_dict) == 2:
        # 세 주사위에서 나온 숫자가 p로 같고 나머지 다른 주사위에서 나온 숫자가 q(p ≠ q)라면 (10 × p + q)2 점을 얻습니다.
        if temp_list[0][1] == 3:
            return (10 * temp_list[0][0] + temp_list[1][0]) ** 2

        # 주사위가 두 개씩 같은 값이 나오고, 나온 숫자를 각각 p, q(p ≠ q)라고 한다면 (p + q) × |p - q|점을 얻습니다.
        if temp_list[0][1] == 2:
            return (temp_list[0][0] + temp_list[1][0]) * abs(temp_list[0][0] - temp_list[1][0])

    # 어느 두 주사위에서 나온 숫자가 p로 같고 나머지 두 주사위에서 나온 숫자가 각각 p와 다른 q, r(q ≠ r)이라면 q × r점을 얻습니다.
    if len(temp_dict) == 3:
        return (temp_list[1][0] * temp_list[2][0])

    # 네 주사위에 적힌 숫자가 모두 다르다면 나온 숫자 중 가장 작은 숫자 만큼의 점수를 얻습니다.
    return min(a, b, c, d)

# print(solution(2, 2, 2, 2))
# print(solution(4, 1, 4, 4))
# print(solution(6, 3, 3, 6))
# print(solution(2, 5, 2, 6))
# print(solution(6, 4, 2, 5))
