# https://school.programmers.co.kr/learn/courses/30/lessons/12901?language=python3
import datetime

def solution(a, b):
    weekday = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    answer = weekday[datetime.datetime(2016, a, b).weekday()]
    return answer

print(solution(5, 24))
