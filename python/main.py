# 프로그래머스
# 같은 숫자는 싫어

def solution(arr):
    answer = []

    seqCheckNum = -1
    for a in arr:
        if seqCheckNum != a:
            answer.append(a)
            seqCheckNum = a

    print(answer)

    return answer


# arr = [1, 1, 3, 3, 0, 1, 1]
# print(arr.count(1))
print(solution([1, 1, 3, 3, 0, 1, 1]))
