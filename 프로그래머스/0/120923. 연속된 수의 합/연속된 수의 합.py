def solution(num, total):
    answer = []
    lst = [i for i in range(-1000, total+1000)]

    for i in range(-1000, len(lst)):
        answer.append(lst[i:i+num])

    for j in answer:
        if sum(j) == total and len(j) == num:
            return sorted(j)