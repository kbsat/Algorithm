# 프로그래머스
# 가운데 글자 가져오기

def solution(s):
    answer = ''
    n = len(s)
    if n % 2 == 0:
        answer = s[n//2-1] + s[n//2]
    else:
        answer = s[n//2]
    return answer


s = "abcde"
print(s[3])

print(solution(s))
