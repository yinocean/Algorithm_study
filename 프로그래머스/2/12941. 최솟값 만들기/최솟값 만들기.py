def solution(A,B):
    answer = 0
    for i, j in zip(sorted(A), sorted(B, reverse=True)):
        answer += i * j
    return answer