# 이코테
# 5-10. 음료수 얼려 먹기

n, m = map(int,input().split())
arr = []

for i in range(n):
    row = list(map(int,input()))
    arr.append(row)

    
visited = [ [False] * m for _ in range(n)]

def dfs(graph, x, y, visited):
    n = len(graph)
    m = len(graph[0])
    
    # 만약 범위를 벗어난 x,y를 골랐다면 중단
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    
    if graph[x][y] == 0 and visited[x][y] == False:
        visited[x][y] = True
        # 상 하 좌 우 순
        dfs(graph,x-1,y,visited)
        dfs(graph,x+1,y,visited)
        dfs(graph,x,y-1,visited)
        dfs(graph,x,y+1,visited)
        return True
    else:
        return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(arr,i,j,visited) == True:
            result += 1

print(result)
    
    
    


    
    
    