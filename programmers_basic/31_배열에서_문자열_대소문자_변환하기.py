# 프로그래머스 코딩 기초 트레이닝 Lv.0 | 배열에서 문자열 대소문자 변환하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181875

def solution(strArr):
    answer = []
    for i in range(len(strArr)):
        if i % 2 == 0:
            answer.append(strArr[i].lower())
        else:
            answer.append(strArr[i].upper())
    return answer
