# 백준 : 2438
#  별찍기 - 1

n = int(input())

for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print()
