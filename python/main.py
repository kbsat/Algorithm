# 백준 - 그래프이론
# 1012. 유기농 배추
import sys

testNum = int(input())
dx = [-1,1,0,0]
dy = [0,0,1,-1]
result = [ 0 for _ in range(testNum)]

def dfs(graph, x, y):
    rowNum = len(graph)
    colNum = len(graph[0])

    if x < 0 or y < 0 or x >= rowNum or y >= colNum:
        return False
    
    if graph[x][y] == 1:
        graph[x][y] = -1

        dfs(graph,x+1,y)
        dfs(graph,x-1,y)
        dfs(graph,x,y+1)
        dfs(graph,x,y-1)
        # for i in range(4):
        #     nx = x + dx[i]
        #     ny = y + dy[i]

        #     dfs(graph,nx,ny)
        
        return True
    return False
    # if graph[x][y] == 0:
    #     return False
    
    # for i in range(4):
    #     nx = x
    #     ny = y

    #     nx += dx[i]
    #     ny += dy[i]

    #     if nx < 0 or ny < 0 or nx >= rowNum or ny >= colNum:

    #         continue
    #     if graph[nx][ny] == 1 :
    #         graph[nx][ny] = -1
    #     elif graph[nx][ny] == 0:
    #         continue
    
    # if graph[x][y] == -1:
    #     return False
    
    # graph[x][y] = -1
    # return True
    

for t in range(testNum):
    m, n, k = map(int,input().split())
    farm = [[0]*m for _ in range(n)]
    for _ in range(k):
        x, y = map(int,input().split())
        farm[y][x] = 1
    

    for i in range(n):
        for j in range(m):
            if dfs(farm, i, j):
                result[t] += 1

    farm = []

for res in result:
    print(res)