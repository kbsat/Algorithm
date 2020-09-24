# 백준 : 5522
# 카드 게임

a = []
sum = 0
for i in range(5):
    a.append(int(input()))
    sum += a[i]

print(sum)
