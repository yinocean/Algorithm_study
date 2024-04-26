from itertools import permutations

def solution(spell, dic):
    res = list(map(''.join, permutations(spell, len(spell))))
    for i in res:
        if i in dic:
            return 1
    return 2

# 수정 전 코드
# def solution(spell, dic):
#     res = list(map(''.join, permutations(spell, len(spell))))
#     for i in res:
#         if i in dic:
#             return 1
#         else:
#             return 2