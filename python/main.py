# 백준 : 8958
# OX 퀴즈

testNum = int(input())
result_list = []
sum = 0
depth = 0
for i in range(testNum):
    answerCheck = list(input())
    for j in range(len(answerCheck)):
        if answerCheck[j] == 'O':
            depth += 1
            sum += depth

        else:
            depth = 0

    result_list.append(sum)
    sum = 0
    depth = 0

for result in result_list:
    print(result)
