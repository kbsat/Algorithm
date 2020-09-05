# 백준 : 2439
#  별찍기 - 2

n = int(input())
space_num = n
for i in range(n):  # n번 반복해줌

    # n-1 ~ 0개의 공백을 찍어줌
    for j in range(space_num-1, 0, -1):
        print(" ", end="")
    for k in range(i+1):  # 1~ n개의 별을 찍어줌
        print("*", end="")
    print()
    space_num -= 1
