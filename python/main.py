# 백준 : 11022
#  A+B-8

T = int(input())
a_list = []
b_list = []
answer = []
for i in range(T):
    a, b = input().split()
    a_list.append(int(a))
    b_list.append(int(b))


for i in range(T):
    answer.append(a_list[i] + b_list[i])
    print("Case #{0}: {1} + {2} = {3}".format(str(i+1),
                                              a_list[i], b_list[i], answer[i]))
