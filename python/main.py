# programmers
# 두 개 뽑아서 더하기
def solution(numbers):
    answer = []
    sortedNumbers = numbers
    sortedNumbers.sort()
    sum = 0
    for i in range(len(sortedNumbers)):
        for j in range(i+1, len(sortedNumbers)):
            sum = sortedNumbers[i] + sortedNumbers[j]
            if sum not in answer:
                answer.append(sum)
    answer.sort()
    return answer


numbers = [2, 1, 3, 4, 1]
solution(numbers)
