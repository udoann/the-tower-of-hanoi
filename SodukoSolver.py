Sodukoboard=[[0,0,0,0,0,0,0,5,0],
             [0,0,8,3,0,0,0,0,1],
             [3,0,0,4,2,5,0,6,0],
             [7,8,5,0,0,3,0,0,4],
             [6,0,0,0,4,0,0,0,9],
             [4,0,0,2,0,0,8,3,6],
             [0,3,0,5,6,8,0,0,2],
             [5,0,0,0,0,4,7,0,0],
             [0,9,0,0,0,0,0,0,0]
]



"""This program sloves a soduko board using recursion and prints its output out"""
def print_sodukoboard(board):
    """This function prints the soduko board to the screen"""
    # loop through the rows.
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        # loops through the columns.
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:  # so the Pipe wouldn't be added at the aend
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")  #made it a string so i can adda space.



#print_sodukoboard(Sodukoboard)
def is_empty(board):
    """checks for empty spaces in board"""
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j) # row, column
    return None

def is_valid(board, number, position):
    """check if the number at a position is valid or not"""
    for i in range(len(board[0])):
        #Checks each element in the row
        if board[position[0]][i] == number and position[1] != i:
            return False
    #Check the Column
    for j in range(len(board)):
        if board[j][position[1]] == number and position[0] != j:
            return False
    #Check box
    box_x = position[1] // 3 # picks one out of 9 boxes in terms of x
    box_y = position[0] // 3 # Picks one out of 9 boxes in terms of y
    
    # this loops through box y and x which gives us 0,1,2
    # so multiplying by 3 will give you intended index
    # adding 3 will make the loop step out since range is to n-1 
    for i in range(box_x*3,box_y*3 + 3): 
        for j in range(box_y*3,box_x*3 + 3):
            if board[i][j] == number and (i,j) != position:
                return False
    return True
def solve_soduku(board):
    empty = is_empty(board)
    if not empty:
        return True
    else:
        row, col = empty
    for i in range(1,10):
        if is_valid(board, i, (row,col)):
            # If the number is valid Then insert it
            board[row][col] = i
            if solve_soduku(board):
                return True
            # If it is not valid back track and set to 0
            board[row][col] = 0
    return False

print_sodukoboard(Sodukoboard)
solve_soduku(Sodukoboard)
print()
print_sodukoboard(Sodukoboard)