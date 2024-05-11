def solution(d, budget):
    answer = []
    for i in sorted(d):
        budget -= i
        if budget < 0:
            break
        answer.append(i)
    return len(answer)