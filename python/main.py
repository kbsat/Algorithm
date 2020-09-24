# 백준 : 2845
# 파티가 끝나고 난 뒤

L, P = map(int, input().split())
guess_nums = list(map(int, input().split()))

people_num = L * P
for guess_num in guess_nums:
    print(str(guess_num - people_num), end=" ")
