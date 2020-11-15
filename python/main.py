# 프로그래머스
# 두 정수 사이의 합

def solution(a, b):
    answer = 0
    if a > b:
        tmp = a
        a = b
        b = tmp

    i = a
    while i <= b:
        answer += i
        i += 1
    return answer
