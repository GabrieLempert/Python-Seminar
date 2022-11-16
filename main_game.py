import tkinter as tk


class ComputerLayer:
    def __init__(self, computer_layer, number):
        self.number_label = None
        self.frame = computer_layer
        self.number = number
        self.guess_number = 0
        self.top_grid = tk.Frame(
            master=self.frame,
            relief=tk.RIDGE,
            borderwidth=2
        )

    def computer_header_layer(self, size):
        tk.Label(master=self.frame, text=f"Computer {self.number}", justify="center", font=f"BOLD {size}").pack()

    def playing_grid(self):
        self.number_label = tk.Label(self.top_grid, text=f"The number is: {self.guess_number} ", relief=tk.RIDGE)
        b_label = tk.Label(self.top_grid, text="B", relief=tk.RIDGE, width=10)
        h_label = tk.Label(self.top_grid, text="H", relief=tk.RIDGE, width=10)
        self.top_grid.pack(fill=tk.BOTH)
        self.top_grid.columnconfigure(index=[0, 1, 2], weight=1, minsize=5)
        self.number_label.grid(row=0, column=0, sticky="w")
        b_label.grid(row=0, column=1, sticky="e")
        h_label.grid(row=0, column=2, sticky="e")


class InfoLayer:
    def __init__(self, info_layer, text, label):
        self.frame = info_layer
        self.text = text
        self.btn = tk.Button(master=self.frame, text="Start")
        self.label_computer = label

    def info_grid(self):
        self.frame.columnconfigure([0, 1], weight=1, minsize=250)
        self.frame.rowconfigure(0, weight=1, minsize=100)
        self.label_computer = tk.Label(master=self.frame, text=self.text, width=40)
        self.label_computer.grid(row=0, column=0)
        self.btn.grid(row=0, column=1, sticky="news")


class TopLayer:
    def __init__(self, top_frame):
        self.computer_2_layer = ComputerLayer(
            tk.Frame(master=top_frame, width=200, borderwidth="2", relief=tk.RIDGE, height=200), 2)
        self.computer_1_layer = ComputerLayer(
            tk.Frame(master=top_frame, width=200, borderwidth="2", relief=tk.RIDGE, height=200), 1)
        self.top_frame = top_frame

    def add_info(self, guessed_number, number_guess, number_bulls, number_hits):
        new_frame = tk.Frame(
            master=self.computer_1_layer.frame,
            relief=tk.RIDGE,
            borderwidth=2,
        )
        label_guess = tk.Label(master=new_frame, text=f"Guess-{number_guess}:Number-{guessed_number}", height=4)
        label_bh = tk.Label(master=new_frame, text=f"{number_bulls}", width=5)
        label_bn = tk.Label(master=new_frame, text=f"{number_hits}", justify="center", width=10)
        new_frame.pack(fill=tk.BOTH)
        new_frame.columnconfigure(index=[0, 1, 2], weight=1, minsize=5)
        label_guess.grid(row=0, column=0, sticky="w")
        label_bh.grid(row=0, column=1, sticky="e")
        label_bn.grid(row=0, column=2, sticky="e")


class BottomLayer:
    def __init__(self, bottom_frame):
        self.info_layer = InfoLayer(info_layer=bottom_frame, label=None, text="")
        self.bottom_frame = bottom_frame


class MainWindow:
    def __init__(self, top, bottom):
        self.top = TopLayer(top_frame=top)
        self.bottom = BottomLayer(bottom_frame=bottom)
        self.top.top_frame.pack(fill=tk.BOTH, expand=True)
        self.bottom.bottom_frame.pack(fill=tk.BOTH)

    def top_window(self, number_1):
        # Computer 1

        self.top.computer_1_layer.guess_number = number_1
        self.top.computer_1_layer.frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        self.top.computer_2_layer.guess_number = "1224"

        self.top.computer_2_layer.frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        self.top.computer_1_layer.computer_header_layer(25)
        self.top.computer_1_layer.playing_grid()
        # Computer 2
        self.top.computer_2_layer.computer_header_layer(25)
        self.top.computer_2_layer.playing_grid()

    def bottom_window(self):
        self.bottom.info_layer.info_grid()


class DisplayGame:
    window = tk.Tk()
    window.title("Game Screen")

    def __init__(self):
        self.main_window = MainWindow(bottom=tk.Frame(
            master=self.window,
            height=150,
            relief=tk.RIDGE,
            borderwidth=2
        ), top=tk.Frame(
            master=self.window,
            height=100,
            border=1
        ))

    def display(self, number_1):
        self.window.geometry("800x800")
        self.main_window.top_window(number_1=number_1)
        self.main_window.bottom_window()
        self.window.mainloop()
