# 이코테
# 예제4-2. 시각

n = int(input())
result = 0

for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) + str(m) + str(s):
                result += 1


print(result)