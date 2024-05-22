from functools import reduce

def solution(dots):
    return reduce(lambda a, b : a * b, [x - y for x, y in zip(max(dots), min(dots))])