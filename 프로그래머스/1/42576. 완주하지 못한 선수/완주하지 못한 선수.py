from collections import Counter

def solution(participant, completion):
    answer = []
    participant = Counter(participant)
    completion = Counter(completion)

    participant.subtract(completion)

    return list(participant.elements())[0]