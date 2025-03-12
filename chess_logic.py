def create_board():
    board = [[None for _ in range(8)] for _ in range(8)]
    for i in range(8):
        board[1][i] = "bP"
        board[6][i] = "wP"
    board[0][0], board[0][7] = "bR", "bR"
    board[7][0], board[7][7] = "wR", "wR"
    board[0][1], board[0][6] = "bN", "bN"
    board[7][1], board[7][6] = "wN", "wN"
    board[0][2], board[0][5] = "bB", "bB"
    board[7][2], board[7][5] = "wB", "wB"
    board[0][3], board[7][3] = "bQ", "wQ"
    board[0][4], board[7][4] = "bK", "wK"
    return board

def is_valid_move(board, start, end, turn):
    piece = board[start[0]][start[1]]
    if not piece or piece[0] != turn:
        return False
    
    piece_type = piece[1]
    start_row, start_col = start
    end_row, end_col = end
    
    if start_row == end_row and start_col == end_col:
        return False
    
    if piece_type == "P":
        direction = -1 if turn == "w" else 1
        if start_col == end_col:
            if end_row == start_row + direction and not board[end_row][end_col]:
                return True
            if (start_row == 6 and turn == "w") or (start_row == 1 and turn == "b"):
                if end_row == start_row + 2 * direction and not board[end_row][end_col] and not board[start_row + direction][start_col]:
                    return True
        if abs(start_col - end_col) == 1 and end_row == start_row + direction:
            target = board[end_row][end_col]
            if target and target[0] != turn:
                return True
        if end_row == 0 and turn == "w" or end_row == 7 and turn == "b":
            if abs(start_row - end_row) == 1 and (start_col == end_col or abs(start_col - end_col) == 1):
                return True
        return False
    
    if piece_type == "R":
        target = board[end_row][end_col]
        if target and target[0] == turn:
            return False
        if start_row == end_row:
            step = 1 if end_col > start_col else -1
            for col in range(start_col + step, end_col, step):
                if board[start_row][col]:
                    return False
            return True
        if start_col == end_col:
            step = 1 if end_row > start_row else -1
            for row in range(start_row + step, end_row, step):
                if board[row][start_col]:
                    return False
            return True
        return False
    
    if piece_type == "N":
        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)
        if (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2):
            target = board[end_row][end_col]
            if target and target[0] == turn:
                return False
            return True
        return False
    
    if piece_type == "B":
        if abs(end_row - start_row) == abs(end_col - start_col):
            row_step = 1 if end_row > start_row else -1
            col_step = 1 if end_col > start_col else -1
            row, col = start_row + row_step, start_col + col_step
            while row != end_row:
                if board[row][col]:
                    return False
                row += row_step
                col += col_step
            target = board[end_row][end_col]
            if target and target[0] == turn:
                return False
            return True
        return False
    
    if piece_type == "Q":
        target = board[end_row][end_col]
        if target and target[0] == turn:
            return False
        if start_row == end_row:
            step = 1 if end_col > start_col else -1
            for col in range(start_col + step, end_col, step):
                if board[start_row][col]:
                    return False
            return True
        if start_col == end_col:
            step = 1 if end_row > start_row else -1
            for row in range(start_row + step, end_row, step):
                if board[row][start_col]:
                    return False
            return True
        if abs(end_row - start_row) == abs(end_col - start_col):
            row_step = 1 if end_row > start_row else -1
            col_step = 1 if end_col > start_col else -1
            row, col = start_row + row_step, start_col + col_step
            while row != end_row:
                if board[row][col]:
                    return False
                row += row_step
                col += col_step
            return True
        return False
    
    if piece_type == "K":
        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)
        if row_diff <= 1 and col_diff <= 1:
            target = board[end_row][end_col]
            if target and target[0] == turn:
                return False
            return True
        
        if row_diff == 0 and col_diff == 2:
            print(f"Checking castling: {start} -> {end}, turn={turn}")
            if turn == "w" and start == (7, 4):
                if end == (7, 6):
                    if board[7][5] is None and board[7][6] is None and board[7][7] == "wR":
                        if not is_king_in_check(board, turn):
                            temp_board = [row[:] for row in board]
                            temp_board[7][5] = "wK"
                            temp_board[7][4] = None
                            if not is_king_in_check(temp_board, turn):
                                print("Short castling for white is allowed")
                                return True
                elif end == (7, 2):
                    if board[7][3] is None and board[7][2] is None and board[7][1] is None and board[7][0] == "wR":
                        if not is_king_in_check(board, turn):
                            temp_board = [row[:] for row in board]
                            temp_board[7][3] = "wK"
                            temp_board[7][4] = None
                            if not is_king_in_check(temp_board, turn):
                                print("Long castling for white is allowed")
                                return True
            elif turn == "b" and start == (0, 4):
                if end == (0, 6):
                    if board[0][5] is None and board[0][6] is None and board[0][7] == "bR":
                        if not is_king_in_check(board, turn):
                            temp_board = [row[:] for row in board]
                            temp_board[0][5] = "bK"
                            temp_board[0][4] = None
                            if not is_king_in_check(temp_board, turn):
                                print("Short castling for black is allowed")
                                return True
                elif end == (0, 2):
                    if board[0][3] is None and board[0][2] is None and board[0][1] is None and board[0][0] == "bR":
                        if not is_king_in_check(board, turn):
                            temp_board = [row[:] for row in board]
                            temp_board[0][3] = "bK"
                            temp_board[0][4] = None
                            if not is_king_in_check(temp_board, turn):
                                print("Long castling for black is allowed")
                                return True
            print("Castling is not allowed for this position")
            return False
    
    return False

def is_king_in_check(board, turn):
    king = "wK" if turn == "w" else "bK"
    king_pos = None
    for row in range(8):
        for col in range(8):
            if board[row][col] == king:
                king_pos = (row, col)
                break
        if king_pos:
            break
    if not king_pos:
        return False
    opponent = "b" if turn == "w" else "w"
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece and piece[0] == opponent:
                if is_valid_move(board, (row, col), king_pos, opponent):
                    return True
    return False

def has_legal_moves(board, turn):
    for start_row in range(8):
        for start_col in range(8):
            piece = board[start_row][start_col]
            if piece and piece[0] == turn:
                for end_row in range(8):
                    for end_col in range(8):
                        if is_valid_move(board, (start_row, start_col), (end_row, end_col), turn):
                            temp_piece = board[end_row][end_col]
                            board[end_row][end_col] = piece
                            board[start_row][start_col] = None
                            check = is_king_in_check(board, turn)
                            board[start_row][start_col] = piece
                            board[end_row][end_col] = temp_piece
                            if not check:
                                return True
    return False

def evaluate_board(board, turn):
    score = 0
    piece_values = {"P": 1, "N": 3, "B": 3, "R": 5, "Q": 9, "K": 0}
    bot_color = "b" if turn == "b" else "w"
    opponent_color = "w" if turn == "b" else "b"

    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece:
                value = piece_values[piece[1]]
                if piece[0] == bot_color:
                    score += value
                elif piece[0] == opponent_color:
                    score -= value

    if is_king_in_check(board, bot_color):
        score -= 10

    return score

def get_all_legal_moves(board, turn):
    moves = []
    for start_row in range(8):
        for start_col in range(8):
            piece = board[start_row][start_col]
            if piece and piece[0] == turn:
                for end_row in range(8):
                    for end_col in range(8):
                        if is_valid_move(board, (start_row, start_col), (end_row, end_col), turn):
                            temp_piece = board[end_row][end_col]
                            board[end_row][end_col] = piece
                            board[start_row][start_col] = None
                            if not is_king_in_check(board, turn):
                                score = 0
                                target = temp_piece
                                opponent = "w" if turn == "b" else "b"
                                if target:
                                    if target[1] == "Q": score += 9
                                    elif target[1] == "R": score += 5
                                    elif target[1] == "B" or target[1] == "N": score += 3
                                    elif target[1] == "P": score += 1
                                if is_king_in_check(board, opponent):
                                    score += 10
                                if piece[1] == "P":
                                    direction = -1 if turn == "w" else 1
                                    progress = (start_row - end_row) * direction
                                    score += progress * 0.5
                                moves.append(((start_row, start_col), (end_row, end_col), score))
                            board[start_row][start_col] = piece
                            board[end_row][end_col] = temp_piece
    return moves