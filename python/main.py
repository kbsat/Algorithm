# 백준 : 4344
# 평균은 넘겠지

C = int(input())
answer_list = []
for i in range(C):
    score_list = list(map(int, input().split()))
    student_number = score_list[0]
    score_list.remove(student_number)
    average = sum(score_list) / student_number

    higher_average_num = 0
    for score in score_list:
        if score > average:
            higher_average_num += 1

    higher_average_percent = (higher_average_num / student_number) * 100
    answer_list.append(higher_average_percent)

for answer in answer_list:
    print(format(answer, ".3f")+"%")
