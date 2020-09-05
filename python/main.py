# 백준 : 10871
# X보다 작은 수

n, x = input().split()
n = int(n)
x = int(x)
small_nums = []
nums = input().split()

for num in nums:
    if int(num) < x:
        small_nums.append(num)

for small_num in small_nums:
    print(small_num, end=" ")
