def solution(array, commands):
    answer = []

    for i, j, k in commands:
        answer.append(sorted(array[i-1:j])[k-1])
    return answer

# 해결 전 문제풀이
# def solution(array, commands):
#     answer = []
#     for i, j, k in zip(commands):
#         answer.append(sorted(array[i:j])[k-1])
#         #answer.append(i)
#     return answer