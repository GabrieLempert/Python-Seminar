import tkinter as tk

# Trying to make window for 2 computers and game interface #
window = tk.Tk()
window.geometry("1000x600")
computer_1_side = tk.Frame(master=window, width=150, height=200, bg="red")
computer_1_side.pack(fill=tk.BOTH, side=tk.LEFT,  expand=True)

computer_2_side = tk.Frame(master=window, width=150, height=200, bg="yellow")

game_interface = tk.Frame(master=window, width=200, height=200, bg="blue")
game_interface.pack(fill=tk.BOTH, side=tk.LEFT,  expand=True)
computer_2_side.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

game_interface_bottom = tk.Frame(master=game_interface, width=200, bg="green")
game_interface_top = tk.Frame(master=game_interface, width=200, bg="green")
game_interface_top.pack(fill=tk.BOTH, side=tk.TOP)
game_interface_bottom.pack(fill=tk.BOTH, side=tk.BOTTOM)
# __________Game intreface try 1 _______  #
for i in range(4):
    for j in range(4):
        game_interface_bottom.columnconfigure(i, weight=1, minsize=75)
        game_interface_bottom.rowconfigure(i, weight=1, minsize=50)

        frame = tk.Frame(
            master=game_interface_bottom,
            borderwidth=4
        )

        frame.grid(row=i, column=j, padx=10, pady=10)
        btn = tk.Button(master=frame, text=f"Row {i}\nColumn {j}")
        btn.pack()

window.mainloop()
