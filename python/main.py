# 백준 : 11021
#  A+B-7

T = int(input())
answer = []
for i in range(T):
    a, b = input().split()
    a = int(a)
    b = int(b)
    answer.append(a+b)

for i in range(T):
    print("Case #"+str(i+1)+": "+str(answer[i]))
