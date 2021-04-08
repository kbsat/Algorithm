# 백준 
# 1010. 다리 놓기
# from itertools import combinations

def combi(m,n):
    bunja = 1
    bunmo = 1
    for i in range(n):
        bunja *= m
        m -= 1
    for j in range(n,0,-1):
        bunmo *= n
        n -= 1

    return bunja // bunmo
t = int(input())
for i in range(t):
    n, m = map(int,input().split())
    
    print(combi(m,n))


