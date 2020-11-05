# 프로그래머스
# 2016년

def solution(a, b):
    answer = ''
    week = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    dayNum = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    date = 0
    for i in range(a-1):
        date += dayNum[i]
    date += b-1
    answer = week[(date % 7)]

    return answer


print(solution(1, 1))
