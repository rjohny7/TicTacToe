'''
Tic Tac Toe with a GUI (Graphical User Interface)
'''
from tkinter import *
'''
A class that extend Label, so that the labels
in our GUI have a row and column associated
with them in addition to all the regular
Label things they they inherit from the Label class.
'''
class TTT_Label(Label):

    def __init__(self, row, col, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.row = row
        self.col = col

'''
A class that makes a tic-tac-toe GUI game.
'''
class Tic_Tac_Toe:

    def __init__(self):

        window = Tk()
        window.title("Tic Tac Toe")
        window["background"] = "black"

        #game state
        self.finished = False
        self.labels = []
        self.turn = "X"

        #create 3x3 board game
        for i in range(3):
            row = []
            for j in range(3):
                label = TTT_Label(i, j, window, text=" ",
                                  width = 3, height = 1,
                                  font = ("Helvetica", "100"))
                #place the label on the GUI using a grid layout
                label.grid(row=i, column=j, padx=1, pady=1)
                #bind each label to the left mouse click
                label.bind("<Button-1>", self.handle_mouse_click)
                row.append(label)
            self.labels.append(row) #put the label in self.labels

        #add a label at the bottom of the GUI
        self.win_label = Label(window, text=" ", font=("Helvetica", "40"))
        self.win_label.grid(row=3, column=0, columnspan=3, sticky=W+E)
        
        #add a button to restart the game
        self.restart_label = Label(window, text="New Game",  font=("Helvetica", "40"))
        self.restart_label.grid(row=4, column=0, columnspan=3, sticky=W+E, padx=1, pady=1)
        self.restart_label.config(bg="yellow")
        self.restart_label.bind("<Button-1>", self.handle_restart)
        #start the GUI
        window.mainloop()

    '''
    This is the callback method for when one of the 9 tic-tac-toe
    labels gets clicked.
    '''
    def handle_mouse_click(self, event):
      #if game over do nothing
        if self.finished:
          return
        #get the label that got clicked
        label = event.widget
        #print(label.row, label.col)

        #check if this space is available
        if label["text"] == " ":
            self.make_move(label)
            if not self.finished:
                self.best_move()

    '''
    Update the game state to reflect the current move
    '''
    def make_move(self, label):
        #place the X or O
        label["text"] = self.turn
        #see if game is over
        if self.check_win(label.row, label.col):
            #update the bottom label
            self.win_label["text"] = "Winner: " + self.turn
            self.finished = True
        elif self.check_draw():
            self.win_label["text"] = "Draw!"
            self.finished = True

        #switch whose turn it is
        if not self.finished:
            self.turn = "X" if self.turn == "O" else "O"

    '''
    This is the callback method for when the new game label gets
    clicked
    '''
    def handle_restart(self, event):
        self.finished = False
        for row in self.labels:
            for square in row:
                square["text"] = " "
        self.turn = "X"
        self.win_label["text"] = " "

    '''
    Check if someone has won by making the move they just made.
    '''
    def check_win(self, row, col):

        #did they win across a row
        if self.labels[row][0]["text"] == \
           self.labels[row][1]["text"] == \
           self.labels[row][2]["text"]:
            return True

        #did they win down a col
        elif self.labels[0][col]["text"] == \
             self.labels[1][col]["text"] == \
             self.labels[2][col]["text"]:
            return True
        #did they win on the diagonal
        elif self.labels[0][0]["text"] == \
             self.labels[1][1]["text"] == \
             self.labels[2][2]["text"] != " ": #make sure the diagonal is not all spaces!
            return True
        #did they win on the reverse diagonal
        elif self.labels[2][0]["text"] == \
             self.labels[1][1]["text"] == \
             self.labels[0][2]["text"] != " ": #make sure it is not all spaces
            return True
        return False
    '''
    Check if the game is drawn
    '''
    def check_draw(self):
        for row in self.labels:
            for square in row:
                if square["text"] == " ":   #not a draw yet
                    return False
        return True

    '''
    Make the best move in the board
    '''
    def best_move(self):
        best_score = -100
        move = None
        for row in self.labels:
            for square in row:
                if square["text"] == " ":
                    square["text"] = self.turn
                    score = self.minimax(True, square)
                    square["text"] = " "
                    if score > best_score:
                        best_score = score
                        move = square
        self.make_move(move)

    '''
    Calculate the score for board state given a move
    '''
    def minimax(self, maxizmizing, move):
        if self.check_win(move.row, move.col): #terminal states 
            return 1 if maxizmizing else -1
        if self.check_draw():
            return 0
        #traverse the decision tree
        self.turn = "X" if self.turn == "O" else "O"
        if maxizmizing:
            best_score = 100
            for row in self.labels:
                for square in row:
                    if square["text"] == " ":
                        square["text"] = self.turn
                        score = self.minimax(False, square)
                        square["text"] = " "
                        if score == -1: #already best score
                            self.turn = "X" if self.turn == "O" else "O"
                            return -1
                        if score < best_score:
                            best_score = score
        else:
            best_score = -100
            for row in self.labels:
                for square in row:
                    if square["text"] == " ":
                        square["text"] = self.turn
                        score = self.minimax(True, square)
                        square["text"] = " "
                        if score == 1: #already best score
                            self.turn = "X" if self.turn == "O" else "O"
                            return score
                        if score > best_score:
                            best_score = score
        self.turn = "X" if self.turn == "O" else "O"
        return best_score




def main():
    game = Tic_Tac_Toe()

main()