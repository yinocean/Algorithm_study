def solution(picture, k):
    answer = []
    for row in picture:
        expanded_row = ""
        for pixel in row:
            expanded_row += pixel * k
        for _ in range(k):
            answer.append(expanded_row)
    return answer

# def solution(picture, k):
#     answer = []
#     for i in picture:
#         for j in i:
#             answer.append(j * k)
#     return answer