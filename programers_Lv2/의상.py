def solution(clothes):
    answer = 1
    dict = {}
    for cloth in clothes:
        try:
            dict[cloth[1]] += 1
        except:
            dict[cloth[1]] = 2
    for v in dict.values():
        answer *= v
    
    return answer - 1

print(
    solution(
        [
            ["a", "headgear"],
            ["b", "headgear"],
            ["c", "eyewear"],
            ["d", "eyewear"],
            ["e", "face"],
            ["f", "face"],
        ]
    )
)  # 26
print(
    solution(
        [
            ["yellow_hat", "headgear"],
            ["blue_sunglasses", "eyewear"],
            ["green_turban", "headgear"],
        ]
    )
)  # 5
print(
    solution(
        [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
    )
)  # 3

