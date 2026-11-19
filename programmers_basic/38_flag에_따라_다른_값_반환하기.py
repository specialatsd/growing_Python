# 프로그래머스 코딩 기초 트레이닝 Lv.0 | flag에 따라 다른 값 반환하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181933

def solution(a, b, flag):
    answer = 0
    if flag == True:
        answer = a+b
    else:
        answer = int(a) -b 
    return answer
