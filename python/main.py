# 백준 : 1297
# TV 크기
import math

diagonal, heightRate, widthRate = map(int, input().split())

totalRate = math.pow(heightRate, 2) + math.pow(widthRate, 2)
x = math.sqrt(math.pow(diagonal, 2)/totalRate)
height = x * heightRate
width = x * widthRate

print(int(height), int(width))
