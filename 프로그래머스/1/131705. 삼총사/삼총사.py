from itertools import combinations

def solution(number):
    answer = []
    for i in combinations(number, 3):
        if sum(i) == 0:
            answer.append(i)
    return len(answer)