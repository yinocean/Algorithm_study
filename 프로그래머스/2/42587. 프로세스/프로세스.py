from collections import deque

def solution(priorities, location):
    queue = deque([[i, p] for i, p in enumerate(priorities)])
    print(queue) # deque([[0, 2], [1, 1], [2, 3], [3, 2]])
    order = 0

    while queue:
        value = queue.popleft() # [0, 2]
        flag = False
        for i, priority in queue: # [0, 2]
            if priority > value[1]: # [1, 1] / [2, 3]
                flag = True
                break
        if flag:
            queue.append(value)
        else:
            order += 1
            if value[0] == location:
                return order