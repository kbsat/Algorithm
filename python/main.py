# 백준 : 1110
# 더하기 사이클

n = int(input())  # 26
a_origin = n // 10  # 2
b_origin = n % 10  # 6
i = 0

a = a_origin
b = b_origin
while True:
    i += 1
    c = (a + b) % 10
    a = b
    b = c
    if a == a_origin and b == b_origin:
        break

print(i)
