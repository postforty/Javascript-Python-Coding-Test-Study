# https://school.programmers.co.kr/learn/courses/30/lessons/42584
# 효율성 테스트 실패
# def solution(prices):
#     answer = []

#     for i in range(len(prices)):
#         current_price = prices[i]
#         next_prices = prices[i+1:]
#         second = 0
#         for price in next_prices:
#             if current_price <= price:
#                 second += 1
#                 continue
#             second += 1
#             break
#         answer.append(second)
#     return answer

def solution(prices):
    answer = [0] * len(prices)
    stack = []

    for i, price in enumerate(prices):
        while stack and prices[stack[-1]] > price: # if가 아닌 while을 사용해야함
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)

    while stack:
        i = stack.pop()
        answer[i] = len(answer) - 1 - i

    return answer

# print(solution([1,2,3,2,3]))
# print(solution([4,4,2]))
print(solution([3, 2, 4, 1, 5])) # while 대신 if를 사용하면 안되는 테스트 케이스, 3번 인덱스의 1을 스택에 있는 인덱스 2와 인덱스 1을 모두 비교해야함. if문을 사용하면 인덱스 2만 비교함