def solution(ingredient):
    answer = 0
    
    def func(iter):
        temp = iter[:]
        count = 0 
        for i, v in enumerate(iter):
            try:
                if temp[i] == 1:
                    if temp[i+1] == 2:
                        if temp[i+2] == 3:
                            if temp[i+3] == 1:
                                temp[i] = 0
                                temp[i+1] = 0
                                temp[i+2] = 0
                                temp[i+3] = 0
                                count += 1
                                break
            except:
                break
        temp = [i for i in temp if i != 0]
        return [temp, count]

    lst = ingredient
    while True:
        if '1231' in ''.join(map(str, lst)):
            lst, count = func(lst)
            answer += count
        else:
            return answer

# print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))
# print(solution([1, 3, 2, 1, 2, 1, 3, 1, 2]))
# print(solution([1, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 1]))
print(solution([1,1,2,3,1,2,3,1,2,3,1,2,3,1]))
# print(solution([1,1,2,3,1,1]))