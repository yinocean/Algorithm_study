def solution(my_string):
    answer = [0 for _ in range(52)]
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    for i in my_string:
        # alphabet에서 i를 찾고 해당 인덱스 값의 밸류를 찾아 1 추가
        answer[alphabet.index(i)] += 1
    return answer