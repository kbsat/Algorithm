# 백준 : 1065
# 한수

def isHan(x):
    target = list(map(int, str(x)))
    if x <= 99:
        return True
    elif target[0] - target[1] == target[1] - target[2]:
        return True

    return False


num = int(input())
result = 0
for i in range(1, num+1):
    if isHan(i):
        result += 1

print(result)
