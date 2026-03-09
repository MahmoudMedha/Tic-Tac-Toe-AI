player_symbol = 'O'
ai_symbol = 'X'

def check_winner(b, ai_sym):
    lines = [b[i] for i in range(3)]
    lines += [[b[i][j] for i in range(3)] for j in range(3)]
    lines += [[b[0][0], b[1][1], b[2][2]], [b[0][2], b[1][1], b[2][0]]]
    
    for line in lines:
        if line[0] == line[1] == line[2] != '_':
            return 10 if line[0] == ai_sym else -10
    return 0

def minimax(b, is_max, player_sym, ai_sym):
    score = check_winner(b, ai_sym)
    if score != 0 or not any('_' in row for row in b):
        return score
    
    if is_max:
        best = -1000
        for i in range(3):
            for j in range(3):
                if b[i][j] == '_':
                    b[i][j] = ai_sym
                    best = max(best, minimax(b, False, player_sym, ai_sym))
                    b[i][j] = '_'
        return best
    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if b[i][j] == '_':
                    b[i][j] = player_sym
                    best = min(best, minimax(b, True, player_sym, ai_sym))
                    b[i][j] = '_'
        return best

def get_best_move(board, player_sym, ai_sym):
    best_val, best_move = -1000, None
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = ai_sym
                move_val = minimax(board, False, player_sym, ai_sym)
                board[i][j] = '_'
                if move_val > best_val:
                    best_move, best_val = (i, j), move_val
    return best_move
