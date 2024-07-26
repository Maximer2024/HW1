def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]]
    ]
    return [player, player, player] in win_conditions

def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    while True:
        print_board(board)
        row = int(input(f"Игрок {players[current_player]}, введите номер строки (0, 1, 2): "))
        col = int(input(f"Игрок {players[current_player]}, введите номер столбца (0, 1, 2): "))

        if board[row][col] != " ":
            print("Эта ячейка уже занята. Попробуйте снова.")
            continue

        board[row][col] = players[current_player]

        if check_win(board, players[current_player]):
            print_board(board)
            print(f"Игрок {players[current_player]} выиграл!")
            break

        if check_draw(board):
            print_board(board)
            print("Игра закончилась вничью!")
            break

        current_player = 1 - current_player

tic_tac_toe()