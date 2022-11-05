import tkinter as tk


class ComputerLayer:
    def __init__(self, frame, number):
        self.frame = frame
        self.number = number

    def computer_header_layer(self, size):
        tk.Label(master=self.frame, text=f"Computer {self.number}", justify="center", font=f"BOLD {size}").pack()

    def playing_grid(self):
        top_grid = tk.Frame(
            master=self.frame,
            relief=tk.RIDGE,
            borderwidth=2
        )
        number_label = tk.Label(top_grid, text="The number is: ", relief=tk.RIDGE)
        b_label = tk.Label(top_grid, text="B", relief=tk.RIDGE, width=10)
        h_label = tk.Label(top_grid, text="H", relief=tk.RIDGE, width=10)
        top_grid.pack(fill=tk.BOTH)
        top_grid.columnconfigure([0, 1, 2], weight=1, minsize=5)
        number_label.grid(row=0, column=0, sticky="w")
        b_label.grid(row=0, column=1, sticky="e")
        h_label.grid(row=0, column=2, sticky="e")


def computer_window(window):
    """
    2 computers frame each will show there stats in the game
    """


class InfoLayer:
    def __init__(self, frame, text):
        self.frame = frame
        self.text = text

    def info_grid(self):
        self.frame.columnconfigure([0, 1], weight=1, minsize=250)
        self.frame.rowconfigure(0, weight=1, minsize=100)
        label_computer = tk.Label(master=self.frame, text=self.text, width=40)
        btn = tk.Button(master=self.frame, text="Start")
        label_computer.grid(row=0, column=0)
        btn.grid(row=0, column=1, sticky="nwse")

    def change_text(self, text):
        self.text = text


class MainWindow:
    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom
        self.top.pack(fill=tk.BOTH, expand=True)
        self.bottom.pack(fill=tk.BOTH)

    def top_window(self):
        # Computer 1
        computer_1 = ComputerLayer(tk.Frame(master=self.top, width=200, borderwidth="2", relief=tk.RIDGE, height=200),
                                   1)
        computer_1.frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        computer_2 = ComputerLayer(tk.Frame(master=self.top, width=200, borderwidth="2", relief=tk.RIDGE, height=200),
                                   2)
        computer_2.frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        computer_1.computer_header_layer(25)
        computer_1.playing_grid()
        # Computer 2
        computer_2.computer_header_layer(25)
        computer_2.playing_grid()

    def bottom_window(self, text):
        info = InfoLayer(frame=self.bottom, text=text)
        info.info_grid()


def main():
    """
    main function that runs the program
    """

    window = tk.Tk()
    bottom = tk.Frame(
        master=window,
        height=150,
        relief=tk.RIDGE,
        borderwidth=2
    )
    top = tk.Frame(
        master=window,
        height=100,
        border=1
    )
    number = 0
    window.geometry("800x800")
    main_window = MainWindow(top=top, bottom=bottom)
    main_window.top_window()
    main_window.bottom_window(text=f"Games Played {number}\nComputer Won {number}")
    window.mainloop()
