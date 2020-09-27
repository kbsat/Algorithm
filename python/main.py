# 백준 : 1212
# 8진수 2진수

oct = input()
oct = "0o"+oct

num = int(oct, 8)
print(bin(num)[2:])
