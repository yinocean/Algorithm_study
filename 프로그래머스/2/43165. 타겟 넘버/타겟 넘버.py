from collections import deque
# numbers의 첫 인덱스에서부터 모든 케이스를 확인하고 그 다음 인덱스로 넘어간다는 점에서 bfs
def solution(numbers, target):
    # 큐 생성
    queue = deque([(0, 0)])  # (current_sum, index)
    count = 0
    
    while queue: # 큐가 비지 않을 때까지
        current_sum, index = queue.popleft()
        # 합이 목표값과 같은지 체크 하고 count 증가
        if index == len(numbers):
            if current_sum == target:
                count += 1
        else: # numbers 내 숫자를 더하거나 빼는 경우 모두 큐에 추가
            queue.append((current_sum + numbers[index], index + 1))
            queue.append((current_sum - numbers[index], index + 1))
    
    return count