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

    # Computer 1
    computer_1 = ComputerLayer(tk.Frame(window, width=200, borderwidth="2", relief=tk.RIDGE, height=200), 1)
    computer_1.frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    computer_2 = ComputerLayer(tk.Frame(window, width=200, borderwidth="2", relief=tk.RIDGE, height=200), 2)
    computer_2.frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

    computer_1.computer_header_layer(25)
    computer_1.playing_grid()
    # Computer 2
    computer_2.computer_header_layer(25)
    computer_2.playing_grid()


def info_grid(frame, text):
    frame.columnconfigure([0, 1], weight=1, minsize=250)
    frame.rowconfigure(0, weight=1, minsize=100)
    label_computer = tk.Label(master=frame, text=text, width=40)
    btn = tk.Button(master=frame, text="Start")
    label_computer.grid(row=0, column=0)
    btn.grid(row=0, column=1, sticky="nwse")


def main_window(window):
    """
    main window shows 2 computers and stats in bottom frame
    """
    top = tk.Frame(
        master=window,
        height=100,
        border=1
    )
    top.pack(fill=tk.BOTH, expand=True)
    computer_window(top)

    bottom = tk.Frame(
        master=window,
        height=150,
        relief=tk.RIDGE,
        borderwidth=5
    )
    bottom.pack(fill=tk.BOTH)
    who_won = ""
    info_grid(bottom, f"Game Number: {1}\n" + who_won)


def main():
    """
    main function that runs the program
    """
    window = tk.Tk()
    window.geometry("800x800")
    main_window(window)
    window.mainloop()


main()
