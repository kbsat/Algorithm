# 백준 : 2577
# 숫자의 개수

a = int(input())
b = int(input())
c = int(input())

result = a*b*c
data = list(str(result))
data = list(map(int, data))
space_num = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in data:
    space_num[i] = space_num[i] + 1

for j in space_num:
    print(j)
