import tkinter as tk

# Trying to make window for 2 computers and game interface #
window = tk.Tk()
window.geometry("600x600")
computer_1_side = tk.Frame(master=window, width=200, height=200, bg="red")
computer_1_side.pack(fill=tk.Y, side=tk.LEFT)

computer_2_side = tk.Frame(master=window, width=200, height=200, bg="yellow")

game_interface = tk.Frame(master=window, width=200, height=200, bg="blue")
game_interface.pack(fill=tk.Y, side=tk.LEFT)
computer_2_side.pack(fill=tk.Y, side=tk.LEFT)
# __________Game intreface try 1 _______ דדד #
for i in range(4):
    for j in range(4):
        frame = tk.Frame(
            master=game_interface,
            borderwidth=4
        )
        frame.grid(row=i, column=j)
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack()

window.mainloop()
