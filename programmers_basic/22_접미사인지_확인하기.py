# 프로그래머스 코딩 기초 트레이닝 Lv.0 | 접미사인지 확인하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181908

def solution(my_string, is_suffix):
    answer = 0
    if my_string.endswith(is_suffix):
        return 1
    else:
        return 0
