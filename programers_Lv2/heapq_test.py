import heapq

lst = [1, 2, 3, 9, 10, 12]
heapq.heapify(lst)  # 스코빌 지수를 최소 힙으로 변환


print(lst)
heapq.heappop(lst)
heapq.heappop(lst)
heapq.heappop(lst)
heapq.heappush(lst, 100)
print(lst)
