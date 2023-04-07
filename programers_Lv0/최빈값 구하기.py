def solution(array):
    answer = 0
    set_list = list(set(array))

    if len(set_list) == 1:
        return set_list[0]
    
    set_dict = dict.fromkeys(set_list, 0)

    for i in array:
        set_dict[i] += 1

    set_dict_sort = sorted(set_dict.items(), key = lambda item: item[1], reverse = True) 
    
    if set_dict_sort[0][1] == set_dict_sort[1][1]:
        return -1
    
    print(set_dict_sort)
    answer = set_dict_sort[0][0]

    return answer

print(solution([1, 2, 3, 3, 3, 4]))
# print(solution([1, 1, 2, 2]))
# print(solution([3, 3, 3]))