def solution(s):
    count = 0
    for i in s:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
            if count <= -1:
                return False
    if s[0] == ')' or s[-1] == '(' or count != 0:
        return False
    return True