import tkinter as tk


class StartScreen:
    window = tk.Tk()
    window.geometry("400x300")
    window.wm_attributes("-topmost", 1)
    window.resizable(0, 0)
    window.title("Start Game Screen")

    def __init__(self):
        self.lbl = tk.Label(master=self.window, text="Start Game")
        self.start_btn = tk.Button(master=self.window, text="Start Game")
        self.number_of_digits = tk.Listbox(master=self.window)

    def create_start(self):
        self.lbl.pack()
        self.add_lines()
        self.number_of_digits.pack()
        self.start_btn.pack()
        self.window.mainloop()

    def add_lines(self):
        for i in range(1, 6):
            self.number_of_digits.insert(i, f"Number of digits:{i}")

    def destroy_window(self):
        self.window.destroy()
