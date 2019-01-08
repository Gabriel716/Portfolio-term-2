#Gabriel Harrison
#12/10/2018
#Tic-Tac-Toe

#global constants
X="X"
O="O"
EMPTY=""
TIE="TIE"
NUM_SQUARES=9
def display_instructions():
    print("Welcome to my Tic Tac Toe")
    print("In order to win, you must get 3 in a row")
    print("""

       !!!  * !   * !!!!
       !  ! * !   *    !
       !  ! * !   *   !
        !!! * !   *  !!!!
******************
       !!!  * ! ! * !!!!
         !  * ! ! * !
       !!!  * !!! * !!!
         !  *   ! *   !
       !!!  *   ! * !!!
******************
      !!    * !!!! * ***
     !      *    ! * * *
     ! -!   *   !  *  * 
      !!    *   !  * * *
                     ***
      """)
    print("Prepare yourself!")

def ask_yes_no(question):
    response=None
    while response not in ("y","n"):
        response=input(question).lower()
    return response

def ask_number(question):
    response=None
    while response not in range(low,high):
        response=int(input(question))
    return response

def ask_number(question,low,high):
    """Within a range ask a number"""
    response="9999"
    while True:
        if response.isdigit():
            if int(response) in range (low,high):
                break
            else:
                response=input(question)
        else:
            print("You must enter a number")
            response=input(question)
    return int(response)


def pieces():
     go_first=ask_yes_no("Do you want the first move? (y/n):")
     if go_first=="y":
        print("\n You will need to go first in order to not lose  in three turns")
        user=X
        computer=O
     else:
         print("\n You are very bold to go against my bot as a second turn")
         computer=X
         user=O
     return user,computer

    


def new_board():
    board=[]
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    """Display the game board on screen"""
    print("\n\t",board[0], "l", board[1], "l", board[2])
    print("\t", "---------")
    print("\n\t",board[3], "l",board[4], "l",board[5])
    print("\t","---------")
    print("\n\t",board[6], "l",board[7], "l",board[8], "\n")



def legal_moves(board):
    """Create list of legal moves"""
    moves=[]
    for square in range(len(board)):
        if board[square]==EMPTY:
            moves.append(square)
    return moves
    
def winner(board):
    """Determine the ways of winning"""
    WAYS_TO_WIN=((0,1,2),
                 (3,4,5),
                 (6,7,8),
                 (0,3,6),
                 (1,4,7),
                 (2,5,8),
                 (0,4,8),
                 (2,4,6))
    for row in WAYS_TO_WIN:
        if board[row[0]]==board[row[1]]==board[row[2]] != EMPTY:
            winner=board[row[0]]
            return winner
    if EMPTY not in board:
        return TIE
    return None


def user_move(board,user):
    """User input for placement of sprites"""
    lm=legal_moves(board)
    move=None
    while move not in lm:
        move=ask_number("Where do you want to play?(0-8)",0,NUM_SQUARES)
  
        if move not in lm:
            print("That is not on the screen genius")
    print("Ok")
    return move
    


def next_turn(turn):
    """Switch turns"""
    if turn==X:
        return O
    else:
        return X

turn=X
turn=next_turn(turn)
print(turn)

def congrat_winner(the_winner,computer,user):
    """Congradulations for the winner"""
    if the_winner!=TIE:
        print(the_winner)
    else:
        print("It is a tie")
    if the_winner==computer:
        print("HA HA HA, you're trash!")
        
    elif the_winner==user:
        print("You got lucky...I felt good today")
        
    elif the_winner==TIE:
        print("You thought that was close... I wasn't trying")
        

def computer_move(board,computer,user):
    """Make computer move"""
    #Make a copy of the board
    board=board[:]
    #The best positions, not in order
    BEST_MOVES=(4,0,2,6,8,1,3,5,7)
    print("I shall take",end="")
    #If computer can win, it will
    for move in legal_moves(board):
        board[move]=computer
        if winner(board)==computer:
            print(move)
            return move
        #Undo after checking
        board[move]=EMPTY
    #If the user can win,block
    for move in legal_moves(board):
        board[move]=user
        if winner(board)==human:
            print(move)
            return move
        #Undo after checking
        baord[move]=EMPTY
    #Pick best position if no one can win
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move
    



    

