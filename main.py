import tkinter as tk


def create_header_pack(header, text, size):
    """
    :param header: frame where the label will show
    :param text: the text you want to show
    :param size: the size of the label

    just easier function to create a header for creating headers for functions

    """
    tk.Label(master=header, text=text, justify="center", font=f"BOLD {size}").pack()


def computer_header_layer(computer, number):
    computer_1_top = tk.Frame(master=computer, width=100, bg="green")
    computer_1_top.pack(side=tk.TOP)
    create_header_pack(computer_1_top, f"Computer {number}", 25)


def playing_grid(frame):
    pass


def info_grid(frame, text):
    frame.columnconfigure([0, 1], weight=1, minsize=250)
    frame.rowconfigure(0, weight=1, minsize=100)
    label_computer = tk.Label(master=frame, text=text, width=40)
    btn = tk.Button(master=frame, text="Start")
    label_computer.grid(row=0, column=0)
    btn.grid(row=0, column=1, sticky="nwse")


def computer_window(window):
    """
    2 computers frame each will show there stats in the game
    """
    # Computer 1
    computer_1_side = tk.Frame(
        master=window,
        relief=tk.RIDGE,
        borderwidth=5)
    computer_1_side.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    computer_header_layer(computer_1_side, 1)

    # Computer 2
    computer_2_side = tk.Frame(
        master=window,
        relief=tk.RIDGE,
        borderwidth=5
    )
    computer_2_side.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    computer_header_layer(computer_2_side, 2)


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
    info_grid(bottom, f"Game Number: {1}\nComputer {1} Won!")


def main():
    """
    main function that runs the program
    """
    window = tk.Tk()
    window.geometry("800x800")
    main_window(window)
    window.mainloop()


main()
