from string import ascii_lowercase, ascii_uppercase

def solution(s, n):
    answer = []
    for i in s:
        if i.isupper():
            idx = ascii_uppercase.find(i)
            answer.append(ascii_uppercase[(idx + n) % 26])
        elif i.islower():
            idx = ascii_lowercase.find(i)
            answer.append(ascii_lowercase[(idx + n) % 26])
        elif i == ' ':
            answer.append(' ')
    return ''.join(answer)