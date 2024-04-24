def solution(s):
    s = s.split(' ')
    answer = []
    
    for i in s:
        answer.append(i.capitalize())
        
    return ' '.join(answer)