
board = [ [ " "," "," "] ,[ " "," "," "] ,[ " "," "," "] ] 
status = True

def display_board():
    print(
    "  _    _    _\n",
    "|" + board[0][0] +"| ","|" + board[0][1] +"| ","|" + board[0][2] +"| \n",
    "|_|  |_|  |_|\n",
    " _    _    _\n",
    "|" + board[1][0] +"| ","|" + board[1][1] +"| ","|" + board[1][2] +"| \n",
    "|_|  |_|  |_|\n",
    " _    _    _\n",
    "|" + board[2][0] +"| ","|" + board[2][1] +"| ","|" + board[2][2] +"| \n",
    "|_|  |_|  |_|\n",
    )


def check(pos):
    x=int(pos/3)
    y=pos%3
    check_row(pos,x,y)
    check_col(pos,x,y)
    check_dia()

def check_row(pos,x,y):

    if( board[x][0]==board[x][1] and board[x][1]==board[x][2] ):
        print("win")
        global status 
        status= False


def check_col(pos,x,y):
    if( board[0][y]==board[1][y] and board[1][y]==board[2][y] ):
        print("win")
        global status 
        status= False

def check_dia():
    global status 
    if(board[0][0]==board[1][1] and board[0][0]==board[2][2] and board[0][0]!=" "):
        print("win")
        status= False
    if(board[2][0]==board[1][1] and board[1][1]==board[0][2] and board[1][1]!=" "):
        print("win") 
        status= False

display_board()
size = 9

while(size>0 and status == True):
    if (size%2 and status == True):
        size = size-1
        print("player1:")
        pos = int(input())
        pos=pos-1
        board[int(pos/3)][pos%3] = "X"
        display_board()
        check(pos)
    elif(status == True):
        size = size-1
        print("player2:")
        pos = int(input())
        pos=pos-1
        board[int(pos/3)][pos%3] = "O"
        display_board()
        check(pos)

if size == 0 :
    print("draw")
