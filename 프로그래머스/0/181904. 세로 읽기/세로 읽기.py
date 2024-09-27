def solution(my_string, m, c):
    answer = []
    for i in range(0, len(my_string), m):
        answer.append(my_string[i:m+i])
    return ''.join([i[c-1] for i in answer])