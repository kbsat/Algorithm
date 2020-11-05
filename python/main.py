# 프로그래머스
# 체육복

def solution(n, lost, reserve):
    new_lost = list(set(lost) - set(reserve))
    new_reserve = list(set(reserve) - set(lost))
    answer = n - len(new_lost)

    for lost_one in new_lost:
        if new_reserve.count(lost_one-1) > 0:
            new_reserve.remove(lost_one-1)
            answer += 1
        elif new_reserve.count(lost_one+1) > 0:
            new_reserve.remove(lost_one+1)
            answer += 1
    return answer


print(solution(5, [1, 2, 3], [1, 2, 3]))
