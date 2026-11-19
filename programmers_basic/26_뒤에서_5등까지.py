# 프로그래머스 코딩 기초 트레이닝 Lv.0 | 뒤에서 5등까지
# https://school.programmers.co.kr/learn/courses/30/lessons/181853

def solution(num_list):
    answer = []
    answer = sorted(num_list)
    return answer[:5]
