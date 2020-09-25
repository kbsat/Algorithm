# 백준 : 15727
# 조별과제를 하려는데 조장이 사라졌다

L = int(input())
result = L // 5
if L % 5 != 0:
    result += 1

print(result)
