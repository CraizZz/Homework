print("Крестики нолики!")
print("----------------")
print("Для игры используйте строки 'X' и тсолбцы 'Y'! ")
print("Удачи!")
print("----------------")

tabel = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
]

def print_board(board):
    for row in board:
        for cell in row:
            print(cell, end= " ")
        print()


def check_win(board, player):
    for row in board:
        if row.count(player) == 3:
            return True



    for i in range(3):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
        if board[0][0] == player and board[1][1] == player and board[2][2] == player:
            return True
        if board[0][2] == player and board[1][1] == player and board[2][0] == player:
            return True

current_player = "x"

while True:
    print_board(tabel)
    print(f"Ход игрока {current_player}!")
    row = int(input("Выберите номер строки 'X': ")) - 1
    col = int(input("Выберите номер столбца 'Y': ")) - 1

    if tabel[row][col] != "-":
        print("Ячейка занята!!!")
        continue

    tabel[row][col] = current_player

    if check_win(tabel, current_player):
        print_board(tabel)
        print(f"Игрок {current_player} выиграл!!")
        break

    if all([cell != "-" for row in tabel for cell in row]):
        print_board(tabel)
        print("Ничья!!!")
        break

    current_player = "0" if current_player == "x" else 'x'




