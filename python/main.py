# 백준 : 3003
# 킹,퀸,룩,비숍,나이트,폰

origin_chess = [1, 1, 2, 2, 2, 8]
donghyeok_chess = list(map(int, input().split()))

for i in range(len(donghyeok_chess)):
    print(origin_chess[i] - donghyeok_chess[i], end=" ")
