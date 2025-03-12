def board_to_fen(board, turn):
    fen = ""
    empty = 0
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece:
                if empty > 0:
                    fen += str(empty)
                    empty = 0
                fen += piece[1] if piece[0] == "w" else piece[1].lower()
            else:
                empty += 1
        if empty > 0:
            fen += str(empty)
            empty = 0
        if row < 7:
            fen += "/"
    fen += " " + turn + " KQkq - 0 1"  # Simplified FEN, without detailed castling
    return fen