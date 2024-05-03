from itertools import combinations

def solution(numbers):
    answer = []
    for i in list(combinations(numbers, 2)):
        answer.append(sum(i))
    return sorted(set(answer))