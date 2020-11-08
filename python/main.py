# X 코테 7번

def solution(n, horizontal):
    answer = [[0]*n for _ in range(n)]
    cussor_x = 0
    cussor_y = 0
    count = 1
    #  dir == -1 이면 좌하로 이동
    #  dir == 1 이면 우상으로 이동
    #  dir == 0 이면 0이 아닌 벡터 한칸 이동
    dir = 0  # > 우 상으로 이동해야함
    if horizontal == True:
        cussor_y = 1
        dir = -1
    else:
        cussor_x = 1
        dir = 1
    answer[cussor_x][cussor_y] = count

    while answer[n-1][n-1] == 0:
        if dir == 1:
            cussor_x -= 1
            cussor_y += 1
            count += 2
            if not check_dir(n, dir, cussor_x, cussor_y):
                dir = 0
        elif dir == -1:
            cussor_x += 1
            cussor_y -= 1
            count += 2
            if not check_dir(n, dir, cussor_x, cussor_y):
                dir = 0
        else:
            if cussor_y == 0 or cussor_x == n-1:
                if cussor_x != n-1:
                    cussor_x += 1
                    dir = 1
                else:
                    cussor_y += 1
                    dir = 1
            elif cussor_x == 0 or cussor_y == n-1:
                if cussor_y != n-1:
                    cussor_y += 1
                    dir = -1
                else:
                    cussor_x += 1
                    dir = -1
            count += 1

        answer[cussor_x][cussor_y] = count

    return answer


def check_dir(n, dir, x, y):
    if dir == 1:
        if x-1 >= 0 and y+1 < n:
            return True
        else:
            return False
    elif dir == -1:
        if x+1 < n and y-1 >= 0:
            return True
        else:
            return False


print(solution(4, False))
