# 이코테 
# 4-4. 게임 개발


def changeDirection(d):
    if d == 0:
        return 3
    else:
        return d-1

def getBack(d):
    return changeDirection(changeDirection(d))

n, m = map(int,input().split())
x, y, d = map(int,input().split())
#  a, b는 현재위치를 항상 나타낼 예정

dx = [0,1,0,-1]
dy = [-1,0,1,0]

# 세로 n 가로 m
game_map = [ [0] * m for i in range(n) ]

for i in range(n):
    row = list(map(int,input().split()))
    game_map[i] = row

# 시작 점 done ( map에 2로 표시 )
game_map[x][y] = 2
# 방문한 칸의 수
count = 1
# 왼쪽을 몇번 검사했는지 체크하는 카운트
check_count = 0

# 갈 곳에 대해 정보를 집어넣을 x, y
temp_x, temp_y = x, y
while True:
    # 1. 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 갈 곳을 정함
    dirCandidate = changeDirection(d)
    temp_x += dx[dirCandidate]
    temp_y += dy[dirCandidate]
    
    
    if (temp_x >= 0 and temp_y >= 0 and temp_x < n and temp_y < m) and game_map[temp_x][temp_y] == 0:
        # 2 a. 왼쪽방향에 만약 가보지 않는 칸이 존재 -> 왼쪽방향으로 회전 후 한칸 전진
        d = dirCandidate
        x, y = temp_x, temp_y
        game_map[x][y] = 2
        count += 1
        check_count = 0
    else:
        # 2 b. 왼쪽방향 만약 가보지 않은 칸이 없으면 왼쪽방향으로 회전만 하고 1단계로 돌아감
        d = dirCandidate
        temp_x, temp_y = x,y
        check_count += 1
    
    # 3. 만약 네 방향 모두 가본 칸이거나 바다로 되어있는 칸인 경우 
    # 바라보는 방향을 유지한 채 한칸 뒤로 가고 1단계 반복 뒤쪽 방향이 바다인 칸이면 움직임을 멈춤
    if check_count == 4:
        backDirection = getBack(d)
        temp_x += dx[backDirection]
        temp_y += dy[backDirection]

        if (temp_x >= 0 and temp_y >= 0 and temp_x < n and temp_y < m):
            if game_map[temp_x][temp_y] == 1:
                break
            else :
                x = temp_x
                y = temp_y
                check_count = 0
        else:
            break

print(count)


