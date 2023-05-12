# import heapq
# def heapsort(iterable):
#     heap = []
#     result = []
#     for value in iterable:
#         heapq.heappush(heap, value)
#     for i in range(len(heap)):
#         result.append(heapq.heappop(heap))
#     return result


# def solution(people, limit):
#     answer = 0

#     people = sorted(people)

#     while people:
#         if people[0] + people[-1] <= limit:
#             people = people[1:-1]
#             answer += 1
#         else:
#             people = people[:-1]
#             answer += 1

#     return answer


# 리스트 슬라이싱 방법은 리스트의 일부를 복사하는 것이므로 시간 복잡도가 O(k)입니다.
# 여기서 k는 슬라이스의 길이입니다.
# 따라서 리스트를 슬라이싱할 때마다 새로운 리스트를 만들어야 하므로 시간이 많이 걸립니다.
# 반면에 포인터를 사용하면 리스트를 복사하지 않고 인덱스만 이동하므로 시간 복잡도가 O(1)입니다.
# 그래서 포인터를 사용하는 코드가 더 빠릅니다.
def solution(people, limit):
    answer = 0

    people = sorted(people)
    left = 0
    right = len(people) - 1

    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1
        answer += 1

    return answer


print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))
print(solution([40, 60, 20, 80], 100))
