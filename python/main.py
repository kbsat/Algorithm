# 이코테
# 5-11. 미로탈출

from collections import deque

n, m = map(int,input().split())
arr = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]
for i in range(n):
    row = list(map(int,input()))
    arr.append(row)

def bfs(x,y):
    global count
    q = deque()
    q.append((x,y))
    
    while q:
        x, y = q.popleft()
    
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m :
                continue
            
            if arr[nx][ny] == 0:
                continue

            if arr[nx][ny] == 1:
                arr[nx][ny] = arr[x][y] + 1
                q.append((nx,ny))
        
    
    return arr[n-1][m-1]



print(bfs(0,0))
print(arr)

