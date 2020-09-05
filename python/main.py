x = int(input())
y = int(input())

if x > 0 and y > 0:  # 1사분면
    print(str(1))
elif x < 0 and y > 0:
    print(str(2))
elif x < 0 and y < 0:
    print(str(3))
else:
    print(str(4))
