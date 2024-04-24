def solution(s):
    s = s.split(' ')
    answer = []
    
    for i in s:
        answer.append(i.capitalize())
        
    return ' '.join(answer)
    
# 문제 해결 전 코드
# def solution(s):
#     s = s.split(' ')
#     answer = []
    
#     for i in s:
#         if i[0].islower(): # 첫 글자가 소문자 이기만 하면 title() 함수 사용
#             answer.append(i.title())
#         else:
#             answer.append(i)
#     return ' '.join(answer)
# 공백문자 이후 글자가 알파벳이 아닌 경우 핸들링이 안되서 런타임 에러 발생
