def solution(cacheSize, cities):
    answer = 0
    if cacheSize == 0:
        return len(cities) * 5
    cache = [None] * cacheSize
    low_cities = map(lambda x: x.lower(), cities)
    for v in low_cities:
        try:
            idx = cache.index(v)
            cache.append(cache.pop(idx))
            answer += 1
        except:
            answer += 5
            cache = cache[1:]
            cache.append(v)
        
    return answer

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))	# 50
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"])) # 16
print(solution(5, ["leo", "leo", "leo"])) # 7
print(solution(3, ["a", "b", "c", "a"])) # 16
print(solution(3, ["a", "b", "c", "a", "b"])) # 17
print(solution(3, ["a", "b", "c", "a", "b", "d", "a"])) # 23