import tkinter as tk
from ai import get_best_move, check_winner

board = [['_'] * 3 for _ in range(3)]
buttons = [[None] * 3 for _ in range(3)]
game_active = True
player_symbol = 'O'
ai_symbol = 'X'

COLORS = {
    'bg': '#1e293b',
    'border': '#475569',
    'hover': '#2d3748',
    'x': '#a5b4fc',
    'o': '#f0abfc',
    'text': '#f1f5f9',
    'accent': '#6366f1'
}


class GameButton(tk.Button):
    def __init__(self, parent, command, row, col):
        super().__init__(
            parent,
            text="",
            font=('Helvetica', 48, 'bold'),
            width=3,
            height=1,
            bg=COLORS['bg'],
            fg='white',
            activebackground=COLORS['hover'],
            activeforeground='white',
            relief='flat',
            bd=0,
            highlightthickness=0,
            command=lambda: command(row, col)
        )
        self.enabled = True
        self.symbol = ""
    
    def set_text(self, symbol, color):
        self.symbol = symbol
        self.config(text=symbol, fg=color, state='disabled', disabledforeground=color)

def check_game_over():
    global game_active
    score = check_winner(board, ai_symbol)
    if score == 10:
        result_label.config(text="AI Wins")
        game_active = False
        return True
    elif score == -10:
        result_label.config(text="You Win")
        game_active = False
        return True
    elif not any('_' in row for row in board):
        result_label.config(text="Draw")
        game_active = False
        return True
    return False


def reset_game():
    global board, game_active, player_symbol, ai_symbol
    board = [['_'] * 3 for _ in range(3)]
    game_active = True
    result_label.config(text="")
    
    player_symbol, ai_symbol = ai_symbol, player_symbol
    
    for row in buttons:
        for btn in row:
            btn.enabled = True
            btn.symbol = ""
            btn.config(text="", state='normal')
    
    if ai_symbol == 'X':
        root.after(300, ai_first_move)

def ai_first_move():
    if game_active:
        move = get_best_move(board, player_symbol, ai_symbol)
        if move:
            board[move[0]][move[1]] = ai_symbol
            color = COLORS['x'] if ai_symbol == 'X' else COLORS['o']
            buttons[move[0]][move[1]].set_text(ai_symbol, color)

def on_click(row, col):
    if board[row][col] == '_' and game_active:
        board[row][col] = player_symbol
        color = COLORS['x'] if player_symbol == 'X' else COLORS['o']
        buttons[row][col].set_text(player_symbol, color)
        
        if not check_game_over():
            root.update()
            root.after(200)
            
            move = get_best_move(board, player_symbol, ai_symbol)
            if move:
                board[move[0]][move[1]] = ai_symbol
                ai_color = COLORS['x'] if ai_symbol == 'X' else COLORS['o']
                buttons[move[0]][move[1]].set_text(ai_symbol, ai_color)
                check_game_over()


root = tk.Tk()
root.title("Tic Tac Toe")
root.configure(bg=COLORS['bg'])
root.resizable(True, True)

board_frame = tk.Frame(root, bg=COLORS['bg'])
board_frame.grid(row=0, column=0, padx=40, pady=40)

for i in range(3):
    for j in range(3):
        border_frame = tk.Frame(board_frame, bg=COLORS['border'], padx=2, pady=2)
        border_frame.grid(row=i, column=j, padx=4, pady=4)
        buttons[i][j] = GameButton(border_frame, on_click, i, j)
        buttons[i][j].pack()

control_frame = tk.Frame(root, bg=COLORS['bg'])
control_frame.grid(row=1, column=0, pady=30)

result_label = tk.Label(control_frame, text="", font=('Helvetica', 32, 'bold'),
                        fg=COLORS['text'], bg=COLORS['bg'])
result_label.pack(pady=(0, 15))

new_game_btn = tk.Button(
    control_frame,
    text="New Game",
    font=('Helvetica', 14),
    bg=COLORS['accent'],
    fg='white',
    activebackground='#818cf8',
    activeforeground='white',
    relief='flat',
    bd=0,
    padx=30,
    pady=10,
    cursor='hand2',
    command=reset_game
)
new_game_btn.pack()

root.update_idletasks()
x = (root.winfo_screenwidth() - root.winfo_width()) // 2
y = (root.winfo_screenheight() - root.winfo_height()) // 2
root.geometry(f'+{x}+{y}')

root.mainloop()