class Computer:
  def __init__(self):
    #-1 = empty, 0 = O, 1 = X
    self.board = [[-1,-1,-1],
                  [-1,-1,-1],
                  [-1,-1,-1]]
    #user starts off as X
    self.turn = "O"
    #uses a board:move mapping to remember stuff
    self.memory = {}
  def bestMove(self,labels):
    #find the best move given the board position
    best_move = [0,0]
    best_score = -100  #1 wins, -1 loses, 0 draws
    for i in range(3):
      for j in range(3):
        if self.board[i][j] == -1:
          score = self.minimax(self.board,i,j,False,self.turn)
          print(score)
          if score > best_score:
            best_score = score
            best_move = [i,j]
            print(best_move)
    #makes the move in the board
    print(best_score)
    labels[best_move[0]][best_move[1]]["text"] = self.turn
    self.update(best_move[0], best_move[1],self.turn)
    return best_move

  def update(self,row,col,turn):
    #update after  making a move
    self.board[row][col] = 1 if turn == "X" else 0
  def minimax(self,board,row,col,isMax,turn):
    board[row][col] = 0 if turn == "O" else 1
    result = self.endGame(board,row,col,turn)
    if result is not None:
      if result == "O":
          board[row][col] = -1
          return 1
      elif result == "X":
        board[row][col] = -1
        return -1
      else:
        board[row][col] = -1
        return 0  
    best_score = -100 if isMax else 100
    turn = "X" if turn == "O" else "O"
    for i in range(3):
      for j in range(3):
        if self.board[i][j] == -1:
          score = self.minimax(board,i,j,False,turn)
          if isMax:
            best_score = max(score,best_score)
          else:
            best_score = min(score,best_score)
    board[row][col] = -1
    return best_score

  def endGame(self,board,row,col,turn):
    if board[row][0] == \
           board[row][1] == \
           board[row][2]:
      return turn

        #did they win down a col
    elif board[0][col] == \
             board[1][col] == \
             board[2][col]:       
      return turn
        #did they win on the diagonal
    elif board[0][0] == \
             board[1][1] == \
             board[2][2] != " ": #make sure the diagonal is not all spaces        
      return turn
        #did they win on the reverse diagonal
    elif board[2][0] == \
             board[1][1] == \
             board[0][2] != " ": #make sure it is not all space   
      return turn
    elif self.checkDraw(board): #check for draw
      return 0
    else: #game not over
      return None

  def checkDraw(self,board):
    for i in range(3):
      for j in range(3):
        if board[i][j] == -1:
          return False
    return True