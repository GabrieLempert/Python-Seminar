import tkinter as tk


class StartScreen:
    def __init__(self, window):
        self.window = window
        self.lbl = tk.Label(master=self.window, text="Start Game")
        self.start_btn = tk.Button(master=self.window, text="Press Here")

    def create_start(self):
        self.lbl.pack()
        self.start_btn.pack()
        self.window.mainloop()

    def destroy_window(self):
        self.window.destroy()




def start():
    return StartScreen(tk.Tk())
