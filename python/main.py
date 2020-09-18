# 백준 : 3052
# 나머지

num_list = []
after_mod_list = []
for i in range(10):
    num_list.append(int(input()))

for num in num_list:
    after_mod_list.append(num % 42)

result_set = set(after_mod_list)

print(len(result_set))
