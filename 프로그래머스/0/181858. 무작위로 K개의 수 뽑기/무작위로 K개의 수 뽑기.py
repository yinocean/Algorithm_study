def solution(arr, k):
    seen = set()
    answer = []
    for num in arr:
        if num not in seen:
            seen.add(num)
            answer.append(num)
        if len(answer) == k:  # 필요한 k개의 값이 이미 모였으면 반복 종료
            break
    while len(answer) < k:
        answer.append(-1)
    return answer


#def solution(arr, k):
#    answer = list(set(arr)) # [0, 1, 2, 3]
#    print(answer)
#    while len(answer) < k:
#        answer.append(-1)
#    return answer[:k]