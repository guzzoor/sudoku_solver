########
######
#
# Soduko solver with backtracking algorithm
#
# Created by Jonathan Gustafsson.
#
#####
########


#
# Should take input from user and create a board from it.
#
def create_own_board():
    board = []

    for row in range(9):
        row = []
        for col in range(9):
            value = input()
            row.append(int(value))
        board.append(row)
    return board

#
# Test board for validatation of the algorithm
#
def create_board():
    board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]
    return board

#
# Prints the board in a better fasion
#
def print_board(board):
    for row in board:
        print(row)

#
# Check if the board is completed, does not mean it correct
#
def is_solved(board):
    for row in range(0,9):
        for col in range(0,9):
            if(board[row][col] == 0):
                return False
    return True

#
# An ugly way of getting a box
#
def get_box(board, row, col):
    if(row < 3):
        if(col < 3):
            return board[0][0:3] + board[1][0:3] + board[2][0:3]
        elif(col < 6):
            return board[0][3:6] + board[1][3:6] + board[2][3:6]
        else:
            return board[0][6:9] + board[1][6:9] + board[2][6:9]
    elif(row < 6):
        if(col < 3):
            return board[3][0:3] + board[4][0:3] + board[5][0:3]
        elif(col < 6):
            return board[3][3:6] + board[4][3:6] + board[5][3:6]
        else: 
            return board[3][6:9] + board[4][6:9] + board[5][6:9]
    else:
        if(col < 3):
            return board[6][0:3] + board[7][0:3] + board[8][0:3]
        elif(col < 6):
            return board[6][3:6] + board[7][3:6] + board[8][3:6]
        else: 
            return board[6][6:9] + board[7][6:9] + board[8][6:9]

#
# Getting a column 
#
def get_col(board, col):
    col_list = []
    for x in range(0,9):
        col_list.append(board[x][col])
    return col_list

#
# Check wheather the input is correct or not. 
#
def is_valid_input(board, row, col, num):
    box = get_box(board, row, col)
    col_list = get_col(board, col)
    if((num in board[row]) or (num in col_list) or (num in box)):
        return False
    else:
        return True

#
# Solves the entire game
#
def solve(board):

    if(is_solved(board)):
        return True

    for row in range(0,9):
        for col in range(0,9):
            if(board[row][col] == 0):
                for num in range(1,10):
                    if(is_valid_input(board, row, col, num)):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0
                return False

#
# Check if all the boxes are correct
#
def check_boxes(board):
    loop_list = [0, 3, 6]
    for x in loop_list:
        for y in loop_list:
            for num in range(1,10):
                if(get_box(board, x, y).count(num) != 1):
                    return False
    return True

#
# Check if all the columns are correct
#
def check_col(board):
    for col in range(9):
        col_list = get_col(board, col)
        for num in range(1, 10):
            if(col_list.count(num) != 1):
                return False
    return True

#
# Check if all the rows are correct
#
def check_rows(board):
    for row in board:
        for num in range(1,10):
            if(row.count(num) != 1):
                return False
    return True

#
# Check if all the rows, columns and boxes are correct
#
def is_solved_check(board):
    return check_rows(board) and check_col(board) and check_boxes(board)


# --------------------------------- Running ---------------------------------
if __name__=="__main__": 
    board = create_board()
    print("---------------- Starting board --------------")
    print_board(board)
    print()
    solve(board)
    if(is_solved_check(board)):
        print("--------------- Solved board -----------------")
        print_board(board)
    else:
        print("No solution")
    