# 이코테
# 4-3. 왕실의 나이트

input_data = input()
row = int(input_data[1])
col = int(ord(input_data[0]) - ord('a')) + 1

steps = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]

result = 0
for step in steps:
    nextRow = row + step[0]
    nextCol = col + step[1]

    if nextRow >= 1 and nextCol >= 1 and nextRow <= 8 and nextCol <= 8:
        result += 1

print(result)