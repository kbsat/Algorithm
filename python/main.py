# 프로그래머스
# 모의고사

def solution(answers):
    answer = []
    scores = [0, 0, 0]
    first_supoja = [1, 2, 3, 4, 5]
    second_supoja = [2, 1, 2, 3, 2, 4, 2, 5]
    third_supoja = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for enum, ans in enumerate(answers):
        if first_supoja[enum % len(first_supoja)] == ans:
            scores[0] += 1
        if second_supoja[enum % len(second_supoja)] == ans:
            scores[1] += 1
        if third_supoja[enum % len(third_supoja)] == ans:
            scores[2] += 1

    for i in range(len(scores)):
        if max(scores) == scores[i]:
            answer.append(int(i+1))
    return answer


solution([1, 3, 2, 4, 2])
