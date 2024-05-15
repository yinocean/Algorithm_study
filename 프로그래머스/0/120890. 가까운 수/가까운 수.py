def solution(array, n):
    answer = []
    array = sorted(array)
    for i in range(0, len(array)):
        answer.append(abs(array[i]-n))
    return array[answer.index(min(answer))]