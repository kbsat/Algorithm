# 백준 : 1546
# 평균


N = input()
nums = list(map(int, input().split()))

max_num = max(nums)


def changeNum(num):
    global max_num
    return num/max_num * 100


nums = list(map(changeNum, nums))
sum = 0
for num in nums:
    sum += num

print(sum/int(N))
