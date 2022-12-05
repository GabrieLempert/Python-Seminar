import tkinter as tk

window = tk.Tk()
window.geometry("400x400")
frame = tk.Frame(master=window, borderwidth="2", relief=tk.RIDGE)
frame.columnconfigure([0, 1, 2, 3], weight=1, minsize=100)
frame.rowconfigure([0, 1], weight=1, minsize=40)
frame.pack()
for i in range(2):
    for j in range(4):
        label = tk.Label(master=frame, text=f"check_{i}_{j}", relief=tk.RIDGE)
        label.grid(row=i, column=j)


window.mainloop()


