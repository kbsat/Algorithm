# 백준 : 2884
# 알람시계

# 입력한 시, 분 보다 45분 일찍 알람 설정하기

# hour = int(input())
# minute = int(input())
hour, minute = input().split()
hour = int(hour)
minute = int(minute)

# 0<=H<=23 ,0<=M<=59

if minute >= 45:
    minute -= 45
else:
    minute = minute-45+60
    if hour == 0:
        hour = 23
    else:
        hour -= 1

print(str(hour), str(minute))
