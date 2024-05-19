def solution(left, right):
    sol = 0
    for i in range(left, right+1):
        answer = []
        for j in range(1, i+1):
            if i % j == 0:
                answer.append(j)
        if len(answer) % 2 == 0:
            sol += i
        else:
            sol -= i
    return sol