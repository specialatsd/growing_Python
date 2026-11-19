# 프로그래머스 코딩 기초 트레이닝 Lv.0 | 원소들의 곱과 합
# https://school.programmers.co.kr/learn/courses/30/lessons/181929

def solution(num_list):
    i = 1
    for n in num_list:
        i *= n
    if i < sum(num_list)**2:
        return 1
    else:
        return 0
