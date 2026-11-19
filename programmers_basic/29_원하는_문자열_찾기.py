# 프로그래머스 코딩 기초 트레이닝 Lv.0 | 원하는 문자열 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/181878

def solution(myString, pat):
    if pat.lower() in myString.lower():
        return 1
    else:
        return 0
