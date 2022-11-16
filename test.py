import tkinter as tk

window = tk.Tk()

label_guess = tk.Label(master=window, text="guess 1:")
label_bh = tk.Label(master=window, text="number")
label_bn = tk.Label(master=window, text="number")
window.columnconfigure(index=[0,1,2], weight=1, minsize=5)
label_guess.grid(row=0, column=0, sticky="w")
label_bh.grid(row=0, column=1, sticky="e")
label_bn.grid(row=0, column=2, sticky="e")

window.geometry("200x200")
window.mainloop()