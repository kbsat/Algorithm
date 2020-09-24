# 백준 : 2914
# 저작권

A, I = map(int, input().split())
# melody_num / A = I

melody_num = A * (I-1)

print(str(melody_num+1))
