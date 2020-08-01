'''
Tic Tac Toe with a GUI (Graphical User Interface)
'''
from tkinter import *

'''
A class that extend Label, so that the labels
in our GUI have a row and column associated
with them (in addition to all the regular
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
        
        #start the GUI
        window.mainloop()

    '''
    This is the callback method for when one of the 9 tic-tac-toe
    labels gets clicked.
    '''
    def handle_mouse_click(self, event):
        #get the label that got clicked
        label = event.widget
        #print(label.row, label.col)

        #check if this space is available
        if label["text"] == " ":
            #place the X or O
            label["text"] = self.turn

            #see if someone won by making this move
            self.check_win(label.row, label.col)

            #switch whose turn it is
            if self.turn == "X":
                self.turn = "O"
            else:
                self.turn = "X"

    '''
    Check if someone has won by making the move they just made.
    '''
    def check_win(self, row, col):

        #did they win across a row
        if self.labels[row][0]["text"] == \
           self.labels[row][1]["text"] == \
           self.labels[row][2]["text"]:
            #update the bottom label
            self.win_label["text"] = "Winner: " + self.turn 

        #did they win down a col
        elif self.labels[0][col]["text"] == \
             self.labels[1][col]["text"] == \
             self.labels[2][col]["text"]:
            #update the bottom label
            self.win_label["text"] = "Winner: " + self.turn

        #did they win on the diagonal
        elif self.labels[0][0]["text"] == \
             self.labels[1][1]["text"] == \
             self.labels[2][2]["text"] != " ": #make sure the diagonal is not all spaces!
            #update the bottom label
            self.win_label["text"] = "Winner: " +self.turn

        #did they win on the reverse diagonal
        elif self.labels[2][0]["text"] == \
             self.labels[1][1]["text"] == \
             self.labels[0][2]["text"] != " ": #make sure it is not all spaces
            #update the bottom label
            self.win_label["text"] = "Winner: "+ self.turn
        

''''
def main():

    game = Tic_Tac_Toe()

main()
'''''