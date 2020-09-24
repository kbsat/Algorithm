# 백준 : 2475
# 검증수

# 5자리 숫자를 받아서 자리수별로 리스트형성
id = list(map(int, input().split()))

sum = 0
for id_num in id:
    sum += (id_num*id_num)
verify_num = sum % 10
print(verify_num)
