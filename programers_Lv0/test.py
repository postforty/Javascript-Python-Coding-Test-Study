def solution(dots):
    answer = 0

    # 기울기 함수
    def slopee(x1,y1,x2,y2):
        try:
            x = (y2 - y1) / (x2 - x1)
        except:
            return 0
        else:
            return x
    
    x1, y1 = dots[0]
    x2, y2 = dots[1]
    x3, y3 = dots[2]
    x4, y4 = dots[3]

    slopee1 = slopee(x1, y1, x2, y2)
    slopee2 = slopee(x3, y3, x4, y4)
    slopee3 = slopee(x1, y1, x3, y3)
    slopee4 = slopee(x2, y2, x4, y4)

    list = [slopee2, slopee3, slopee4]

    # or 연산자 주의
    if slopee1 == slopee2 or slopee3 == slopee4:
        return 1

    return answer

print(solution([[1, 4], [9, 2], [3, 8], [11, 6]]))
print(solution([[3, 5], [4, 1], [2, 4], [5, 10]]))
# print(solution([[4, 1], [3, 5], [3, 5], [4, 1]]))
# print(solution([[1, 1], [4, 2], [5, 5], [7, 7]]))
# print(solution([[1, 1], [10, 8], [7, 7], [8, 6]]))
