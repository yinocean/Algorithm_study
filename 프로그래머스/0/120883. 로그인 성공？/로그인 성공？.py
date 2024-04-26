def solution(id_pw, db):
    if id_pw in db:
        return "login"
    for i, j in db:
        if id_pw[0] == i and id_pw[1] != j:
            return "wrong pw"
    else:
        return "fail"
    
# testcase 1, 5 error
# def solution(id_pw, db):
#     if id_pw in db:
#         return "login"
#     elif id_pw[0] in [i for i, j in db] and id_pw[1] not in [j for i, j in db]:
#         return "wrong pw"
#     else:
#         return "fail"