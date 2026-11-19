# 프로그래머스 코딩 기초 트레이닝 Lv.0 | 홀짝에 따라 다른 값 반환하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181935

def solution(n):
    answer = 0
    if n % 2 == 0:
        for even in range(2,n+1,2):
            answer += even**2
        return answer
    else:
        for odd in range(1,n+1,2):
            answer += odd
        return answer
