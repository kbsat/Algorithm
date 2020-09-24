# 백준 : 1271
# 엄청난 부자2

n, m = map(int, input().split())

distribution = n // m
remainder = int(n % m)
print(str(distribution))
print(str(remainder))
