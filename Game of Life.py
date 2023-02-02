board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
# Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
N = len(board)
M = len(board[0])

places = [(0, 1), (0, -1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
list = []

for r in range(N):
    for c in range(M):
        count = 0
        for x, y in places:
            if 0 <= r + x < N and 0 <= c + y < M and abs(board[r + x][c + y]) == 1:
                count += 1
        if board[r][c] == 1:
            # That means its a Live Cell
            if count < 2 or count > 3:
                board[r][c] = -1

        elif board[r][c] == 0:
            # That means its a dead cell
            if count == 3:
                board[r][c] = 2

for r in range(N):
    for c in range(M):
        if board[r][c] == -1:
            board[r][c] = 0
        elif board[r][c] == 2:
            board[r][c] = 1

print(board)
