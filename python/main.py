# 이코테
# 3. 숫자 카드 게임

n,m = map(int,input().split())
cards = [[0] * m for _ in range(n)]
min_set = set([])

# 배열입력
for i in range(n):
    cards[i] = list(map(int,input().split()))

print(cards)
for i in range(n):
    min_num = cards[i][0]
    for j in range(m):
        if min_num > cards[i][j]:
            min_num = cards[i][j]
    min_set.add(min_num)

print(max(min_set))
