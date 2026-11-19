# 프로그래머스 코딩 기초 트레이닝 Lv.0 | 수 조작하기 1
# https://school.programmers.co.kr/learn/courses/30/lessons/181926

def solution(n, control):
    for w in control:
        if w == 'w':
            n += 1
        elif w == 's':
            n -= 1
        elif w == 'd':
            n += 10
        else: 
            n -= 10
    return n
