def solution(arr, intervals):
    answer = []
    for i, j in intervals:
        answer.append(arr[i:j+1])
    return answer[0] + answer[1]