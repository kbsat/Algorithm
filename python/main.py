# 백준 : 4673
# 셀프 넘버

def d(n):
    sn = str(n)
    result = n
    for sn_element in sn:
        result += int(sn_element)

    return result


origin = list(range(1, 10001))
for i in range(1, 10001):
    if d(i) in origin:
        origin.remove(d(i))

for i in origin:
    print(i)
