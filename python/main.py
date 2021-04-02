# 이코테
# 4. 1이 될 때까지

N, K = map(int,input().split())
count = 0
while N>=2 :
    if N % K == 0:
        N = N // K
    else :
        N = N - 1
    count += 1

print(count)