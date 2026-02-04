import tkinter as tk
board=[
    ["","",""],["","",""],["","",""]
]
current_Player="X"
window=tk.Tk()
window.title("Tic Tac Toe")
window.geometry("310x400")

result_label=tk.Label(window,text="Player X's turn",font=("Arial",16))
result_label.grid(row=0,column=0,columnspan=3)
buttons=[[None for _ in range(3)] for _ in range(3)]
def reset_game():
    global current_Player,board
    current_Player="X"
    board=[
       ["","",""],["","",""],["","",""]
    ]
    result_label.config(text="Player X's turn")
    for row in buttons:
        for button in row:
            button.config(text="",state="normal")
def disable_buttons():
    for row in buttons:
        for button in row:
            button.config(state="disabled")
def on_click(row,col):
    global current_Player
    if buttons[row][col]["text"]=="":
        buttons[row][col]["text"]=current_Player
        board[row][col]=current_Player
        winner=check_winner(board)
        if winner:
            result_label.config(text=f"player {winner} wins")
            disable_buttons()
        elif is_draw(board):
            result_label.config(text="its a draw")
            disable_buttons()
        else:
            current_Player="0" if current_Player=="X" else "X"
            result_label.config(text=f"player {current_Player} turn")
def create_board():
    for row in range(3):
        for col in range(3):
            buttons[row][col]=tk.Button(window,text="",font=("Arial",24),height=2,width=5,command=lambda r=row,c=col:on_click(r,c))
            buttons[row][col].grid(row=row+1,column=col)
def check_winner(board):
    for row in board:
        if row[0]==row[1]==row[2] and row[0]!="":
            return row[0]
    for col in range(3):
        if board[0][col]==board[1][col]==board[2][col] and board[0][col]!="":
            return board[0][col]
    if board[0][0]==board[1][1]==board[2][2] and board[0][0]!="":
        return board[1][1]
    if board[0][2]==board[1][1]==board[2][0] and board[0][2]!="":
        return board[1][1]
    return None
def is_draw(board):
    for row in board:
        for cell in row:
            if cell=="":
                return False
    return True
create_board()
reset_button=tk.Button(window,text="reset game",font=("Arial",16),command=reset_game)
reset_button.grid(row=4,column=0,columnspan=3)
window.mainloop()