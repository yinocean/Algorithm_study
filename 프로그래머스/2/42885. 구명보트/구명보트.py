def solution(people, limit):
    people.sort()  # 몸무게 순으로 정렬 [50, 50, 70, 80]
    left, right = 0, len(people) - 1  # 양쪽 끝 인덱스 설정
    boat_count = 0  # 보트의 개수를 카운트

    while left <= right:
        # 가장 가벼운(left) 사람과 가장 무거운(right) 사람을 한 보트에 태울 수 있는지 확인
        if people[left] + people[right] <= limit:
            left += 1  # 함께 탈 수 있다면 가벼운 사람을 다음 인덱스로 이동
        right -= 1  # 무거운 사람은 무조건 태우고 다음으로 이동
        boat_count += 1  # 보트 수 증가

    return boat_count

# 2
# def solution(people, limit):
#     people.sort() # 사람들을 오름차순으로 정렬 [50, 50, 70, 80]
#     boat_count = 0 # 구명보트의 갯수를 선언
#     total = 0 # 몸무게 합 체크하는 인덱스 변수 total 선언
    
#     # total 인덱스가 전체 리스트 길이를 넘지 않을 때까지 반복
#     while total < len(people):
#         # 두 명 무게가 limit 이하면 # [50, 50, 70, 80]
#         if total + 1 < len(people) and people[total] + people[total + 1] <= limit:
#             total += 2  # 두 명 태우고 다음으로 넘어감
#         else:
#             total += 1  # 제한 넘으면 한 명만 태움
#         boat_count += 1

#     return boat_count


# #1
# def solution(people, limit): # [70, 50, 80, 50]
#     total = 0 # 몸무게 합 체크하는 변수 total 선언
#     boat_count = 1 # 구명보트의 갯수를 선언
#     people.sort() # 사람들을 오름차순으로 정렬 [50, 50, 70, 80]
    
#     for i in people: # 오름차순으로 정렬된 사람들을 돌면서 가벼운 사람부터 구명보트에 태우는데
#         total += i
#         #print(total, i)
#         if total >= limit: # 주어진 무게 제한에 걸릴 때
#             boat_count += 1 # 구명보트는 하나씩 추가된다
#             #print(boat_count)
#             total = 0 # 구명보트 갯수가 증가하면 몸무게 제한은 리셋
#     return boat_count