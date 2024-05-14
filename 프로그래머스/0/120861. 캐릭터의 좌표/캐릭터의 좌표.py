def solution(keyinput, board):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    move_types = ['up', 'down', 'left', 'right']
    x, y = 0, 0
    
    for move in keyinput: 
        for i in range(len(move_types)):
            if move == move_types[i]:
                nx = x + dx[i]
                ny = y + dy[i]
                
        if nx < -(board[0]//2) or ny < -(board[1]//2) or nx > board[0]//2 or ny > board[1]//2:
            continue
        x, y = nx, ny
    return [x, y]
    #return [-(board[0]//2),-(board[1]//2)]

# 처음 코드
# def solution(keyinput, board):
#     dx = [0, 0, -1, 1]
#     dy = [1, -1, 0, 0]
#     move_types = ['up', 'down', 'left', 'right']
#     x, y = 0, 0
    
#     for move in keyinput: 
#         for i in range(len(move_types)):
#             if move == move_types[i]:
#                 nx = x + dx[i]
#                 ny = y + dy[i]
                
#         if nx == -board[0]//2 or ny == -board[1]//2 or nx == board[0]//2 or ny == board[1]//2:
#             continue
#         x, y = nx, ny
#     return [x, y]