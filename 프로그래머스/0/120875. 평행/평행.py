def solution(dots):
    [[x1, y1], [x2, y2], [x3, y3], [x4, y4]] = dots
    if (x1 - x2) / (y1 - y2) == (x3 - x4) / (y3 - y4):
        return 1
    elif (x1 - x3) / (y1 - y3) == (x2 - x4) / (y2 - y4):
        return 1
    elif (x1 - x4) / (y1 - y4) == (x2 - x3) / (y2 - y3):
        return 1
    return 0