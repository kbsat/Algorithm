# 이코테
# 예제4-1. 상하좌우
# U D L R

# 내 풀이
# n = int(input())
# movList = input().split()
# print(n,movList)

# x, y = 1, 1
# canMove = [-1, 0, -1, 0]

# for mov in movList:
#     if mov == 'U' and canMove[0] == 0: 
#         x -= 1
#     elif mov == 'D' and canMove[1] == 0 :
#         x += 1
#     elif mov == 'L' and canMove[2] == 0:
#         y -= 1
#     elif mov == 'R' and canMove[3] == 0 :
#         y += 1

    
#     canMove = [0,0,0,0]
#     if x == 1:
#         canMove[0] = -1
#     elif x == n:
#         canMove[1] = -1
    
#     if y == 1:
#         canMove[2] = -1
#     elif y == n:
#         canMove[3] = -1

# print(x,y)



# 답 풀이
n = int(input())
x, y = 1, 1
plans = input().split()

# moveTypes에 따른 변화량
dx = [-1,1,0,0]
dy = [0,0,-1,1]
moveTypes = ['U','D','L','R']

for plan in plans:
    for i in range(len(moveTypes)):
        if plan == moveTypes[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            break
    
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x,y = nx,ny

print(x,y)
        