# tic-tac-toe
def rwo_winner(board, symbol):
    for row in board:
        if row.count(symbol) == 3:
            return True

    return False

def col_winner(board, symbol):
    for col_ined in range(3):
        count = 0
        for row in range(3):
            if board[row][col_ined] == symbol:
                count += 1
        if count == 3:
            return True
    return False

def diagonal_winner(board, symbol):
    primary_diagonal = 0
    secondary_diagonal = 0
    for index in range(3):

        if board[index][index] == symbol:
            primary_diagonal = 1
        if board[index][3 - index - 1] == symbol:
            secondary_diagonal = 1

    if primary_diagonal == 3 or secondary_diagonal == 3:
        return True
    return False



def chek_winner(board, symbol):
    if_row_winner = rwo_winner(board, symbol)
    if_col_winner = col_winner(board, symbol)
    if_diagonal_winner = diagonal_winner(board, symbol)

    if if_row_winner or if_col_winner or if_diagonal_winner:
        return True
    return False





def print_bord(board):
    for row in board:
        print(" | ".join(row), " | ")

print("Play with tic-tac-toe")

player_one_name = input("Player One name: ")
player_two_name = input("Player Two name: ")

player_one_symbol = input(f"{player_one_name} would you like to play with 'X' or 'O").upper()

player_two_symbol = 'O' if player_one_symbol == 'X' else 'X'

print("this is the numeration of the board")
print("| 1 | 2 | 3 ")
print("| 4 | 5 | 6 ")
print("| 7 | 8 | 9 ")
print(f"{player_one_name} start first")
mapper = {
    1: (0,0),
    2: (0,1),
    3: (0,2),
    4: (1,0),
    5: (1,1),
    6: (1,2),
    7: (2,0),
    8: (2,1),
    9: (2,2),
}
game = 1
board = [[" ", " "," "]
         for _ in range(3)]
while game < 10:

    current_player = player_one_name if game % 2 != 0 else player_two_name
    current_symbol = player_one_symbol if game % 2 != 0 else player_two_symbol

    try:
        position = int(input(f"{current_player}' choose a free position [1-9]"))

    except ValueError:
        print("Please enter a valid number")
        continue

    if not (0 <= position <= 9):
        print("Please enter a valid number, between 1 and 9")
        continue


    row, col = mapper[position]
    if board[row][col] != " ":
        continue
    board[row][col] = current_symbol

    if game >= 5 and chek_winner(board, current_symbol):
        print_bord(f"{current_player} is a winner!")
        break



    game += 1
    print_bord(board)
else:
    print("thank you for playing")
