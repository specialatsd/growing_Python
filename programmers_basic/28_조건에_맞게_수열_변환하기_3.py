# 프로그래머스 코딩 기초 트레이닝 Lv.0 | 조건에 맞게 수열 변환하기 3
# https://school.programmers.co.kr/learn/courses/30/lessons/181835

def solution(arr, k):
    answer = []
    for n in arr:
        if k % 2 == 0:
            answer += [n + k]
        else:
            answer += [n * k]
    return answer
