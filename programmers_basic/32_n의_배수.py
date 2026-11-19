# 프로그래머스 코딩 기초 트레이닝 Lv.0 | n의 배수
# https://school.programmers.co.kr/learn/courses/30/lessons/181937

def solution(num, n):
    answer = 0
    if num % n == 0:
        return 1
    else: 
        return 0
