# 프로그래머스 코딩 기초 트레이닝 Lv.0 | A 강조하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181874

def solution(myString):
    answer = ''
    for n in myString.lower():
        if n == 'a':
            answer += n.upper()
        else:
            answer += n
    return answer
