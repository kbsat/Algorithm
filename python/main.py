# 백준
# 2480. 주사위 세개

a,b,c = map(int,input().split())
aList = [a,b,c]
dic = {}
result = 0

for num in aList:
    if num in dic:
        dic[num] += 1
    else:
        dic[num] = 1

if len(dic) == 1:
    result = aList[0] * 1000 + 10000
elif len(dic) == 2:
    for k, v in dic.items():
        if v == 2:
            result = k * 100 + 1000
else:
    result = max(aList) * 100

print(result)
