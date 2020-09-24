# 백준 : 5554
# 심부름 가는 길

one = int(input())
two = int(input())
three = int(input())
four = int(input())

sum = one+two+three+four
minute = sum // 60
second = sum % 60

print(minute, second, sep="\n")
