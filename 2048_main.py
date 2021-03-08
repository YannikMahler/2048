import tkinter as tk
import random

GRID_COLOR = "#a39489"
EMPTY_CELL_COLOR = "#c2b3a9"
SCORE_LABEL_FONT = ("Verdana", 24)
SCORE_FONT = ("Helvetica", 36, "bold")
GAME_OVER_FONT = ("Helvetica", 48, "bold")
GAME_OVER_FONT_COLOR = "ffffff"
WINNER_BG = "#ffcc00"
LOSER_BG = "#a39489"


CELL_COLORS = {
    2: "#00c7ff",
    4: "#00c7ff",
    8: "#3eadfa",
    16: "#3eadfa",
    32: "#6d90e9",
    64: "#6d90e9",
    128: "#9170cb",
    256: "#9170cb",
    512: "#a74da1",
    1024: "#a74da1",
    2048: "#ac256f"
}

CELL_NUMBER_COLOR = {
    2: "#a6a6a6",
    4: "#a6a6a6",
    8: "#fffff",
    16: "#fffff",
    32: "#fffff",
    64: "#fffff",
    128: "#fffff",
    256: "#fffff",
    512: "#fffff",
    1024: "#fffff",
    2048: "#fffff"
}

CELL_NUMBER_FONTS = {
    2: ("Helvetica", 55, "bold"),
    4: ("Helvetica", 55, "bold"),
    8: ("Helvetica", 55, "bold"),
    16: ("Helvetica", 50, "bold"),
    32: ("Helvetica", 50, "bold"),
    64: ("Helvetica", 50, "bold"),
    128: ("Helvetica", 45, "bold"),
    256: ("Helvetica", 45, "bold"),
    512: ("Helvetica", 45, "bold"),
    1024: ("Helvetica", 40, "bold"),
    2048: ("Helvetica", 40, "bold")
}
class Game(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title("2048 by Yannik")

        self.main_grid = tk.Frame(
            self, bg=GRID_COLOR, bd=3, height=600, width=400
        )
        self.main_grid.grid(pady=(100, 0))
        self.make_GUI()
        self.start_game()

        self.mainloop()



def make_GUI(self):
    self.cells = []
    for i in range(4):
        row = []
        for j in range(4):
            cell_frame = tk.Frame(
                self.main_grid,
                bg=EMPTY_CELL_COLOR,
                width=150,
                height=150,
            )
            cell_frame.grid(row=i, column=j, padx=5, pady=5)
            cell_number = tk.Label(self.main_grid, bg=EMPTY_CELL_COLOR)
            cell_number.grid(row=i, column=j)
            cell_data = {"frame": cell_frame, "number": cell_number}
            row.append(cell_data)
        self.cells.append(row)

    #Header/ Scoreboard
    score_frame = tk.Frame(self)
    score_frame.place(relx=0.5, y=45, anchor="center")
    tk.Label(
        score_frame,
        text="Score",
        font=SCORE_LABEL_FONT,
    ).grid(row=0)
    self.score_label = tk.Label(score_frame, text="0", font=SCORE_FONT)
    self.score_label.grid(row=1)

def start_game(self):
    self.matrix = [[0] * 4 for _ in range(4)]

    row = random.randint(0, 3)
    col = random.randint(0, 3)
    self.matrix[row][col] = 2
    self.cells[row][col]["frame"].configure(bg=CELL_COLORS[2])
    self.cells[row][col]["number"].configure(
        bg=CELL_COLORS[2],
        fg=CELL_NUMBER_COLOR[2],
        font=CELL_NUMBER_FONTS[2],
        text="2"
    )

    while self.matrix[row][col] !=0:
        row = random.randint(0, 3)
        col = random.randint(0, 3)
        self.matrix[row][col] = 2
        self.cells[row][col]["frame"].configure(bg=CELL_COLORS[2])
        self.cells[row][col]["number"].configure(
            bg=CELL_COLORS[2],
            fg=CELL_NUMBER_COLOR[2],
            font=CELL_NUMBER_FONTS[2],
            text="2"
        )

    #Matrix Manipulation Funktion
    def stack(self):
        new_matrix = [[0] * 4 for _ in range(4)]
        for i in range(4):
            fill_position = 0
            for j in range(4):
                if self.matrix[i][j] !=0:
                    new_matrix[i][fill_position] = self.matrix[i][j]
                    fill_position += 1
        self.matrix = new_matrix


    def combine(self):
        for i in range(4):
            for j in range(3):
                if self.matrix[i][j] != 0 and self.matrix[i][j] == self.matrix[i][j + 1]:
                    self.matrix[i][j] *= 2
                    self.matrix[i][j + 1] = 2
                    self.score += self.matrix[i][j]


    def reverse(self):
        new_matrix = []
        for i in range(4):
            new_matrix.append([])
            for j in range(4):
                new_matrix[i].append(self.matrix[i][3 - j])
        self.matrix = new_matrix

    def transpose(self):
        new_matrix = [[0] * 4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                new_matrix[i][j] = self.matrix[j][i]
        self.matrix = new_matrix


    #Hinzufügen von tiles [2 oder 4]
    def add_new_tile(self):
        row = random.randint(0, 3)
        col = random.randint(0, 3)
        while (self.matrix[row][col] != 0):
            row = random.randint(0, 3)
            col = random.randint(0, 3)
        self.matrix[row][col] = random.choice([2, 4])

    #Update GUI
    def update_GUI(self):
        for i in range(4):
            for j in range(4):
                cell_value = self.matrix[i][j]
                if cell_value == 0:
                    self.cells[i][j]["frame"].configure(bg=EMPTY_CELL_COLOR)
                    self.cells[i][j]["number"].configure(bg=EMPTY_CELL_COLOR, text="")
                
