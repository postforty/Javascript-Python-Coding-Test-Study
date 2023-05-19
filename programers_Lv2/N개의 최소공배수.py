from functools import reduce

def solution(arr):
    max_num = reduce((lambda x, y: x * y if x else 1), arr, 1)
    # for i in arr:
    #     max_num *= i
    for i in range(max(arr), max_num+1):
        result = 0
        for j in arr:
            if i % j != 0:
                result += 1
        if result == 0:
            return i

print(solution([2,6,8,14])) # 168
print(solution([1,2,3])) # 6
print(solution([5,10,15,20,25])) # 300
# print(solution([1,10,100,1000,5000,3,9999])) # 49995000
print(solution([1,2,3,4,5,6,7,8,9,10])) # 2520


