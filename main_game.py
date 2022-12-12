import tkinter as tk
from tkinter import messagebox


class ComputerLayer:
    """
    A class use to build the frames and the labels of the computer
    ...
    Methods
    -------
    __init__(self, computer_layer, number)
    computer_header_layer(self, size)
    playing_grid(self)
    """

    def __init__(self, computer_layer, computer_number):
        """ The function is building ComputerLayer, constructor
            :parameters: self: the function gets self as a parameter
            computer_layer: the frame of the layer
            number: the id number of the computer
            :returns: the function do not return any value
         """
        self.number_label = None
        self.frame = computer_layer
        self.computer_number = computer_number
        self.top_grid = tk.Frame(
            master=self.frame,
            relief=tk.RIDGE,
            borderwidth=2
        )

    def computer_header_layer(self, size):
        """ The function is building the label of the computer layer
            :parameters: self: the function gets self as a parameter
            size: the label size
            :returns: the function do not return any value
        """

        tk.Label(
            master=self.frame,
            text=f"Computer {self.computer_number + 1}",
            justify="center", font=f"BOLD {size}") \
            .pack()

    def playing_grid(self):
        """ The function is building the ComputerLayer grid
            :parameters: self: the function gets self as a parameter
            :returns: the function do not return any value
        """

        self.number_label = tk.Label(self.top_grid, text=f"The number is:PRESS START", relief=tk.RIDGE)
        b_label = tk.Label(self.top_grid, text="B", relief=tk.RIDGE, width=5)
        h_label = tk.Label(self.top_grid, text="H", relief=tk.RIDGE, width=5)
        self.top_grid.pack(fill=tk.BOTH)
        for i in range(3):
            self.top_grid.columnconfigure(index=int(i), weight=1, minsize=5)
        self.number_label.grid(row=0, column=0, sticky="w")
        b_label.grid(row=0, column=1, sticky="e")
        h_label.grid(row=0, column=2, sticky="e")


class InfoLayer:
    """
    A class use to build the frames and the labels of the bottom layer
    ...
    Methods
    -------
    __init__(self, info_layer, text, label)
    def info_grid(self)
    """

    def __init__(self, info_layer, text, label):
        """ The function is building InfoLayer, constructor
            :parameters: self: the function gets self as a parameter
            info_layer:
            text:
            label:
            :returns: the function do not return any value
        """

        self.frame = info_layer
        self.text = text
        self.start_btn = tk.Button(master=self.frame, text="Start")
        self.stats_btn = tk.Button(master=self.frame, text="To Stats")
        self.back_to_btn = tk.Button(master=self.frame, text="Back")
        self.label_computer = label

    def info_grid(self):
        """ The function is building the InfoLayer grid
            :parameters: self: the function gets self as a parameter
            :returns: the function do not return any value
        """
        for i in range(4):
            self.frame.columnconfigure(i, weight=1, minsize=150)
        self.frame.rowconfigure(0, weight=1, minsize=100)
        self.label_computer = tk.Label(master=self.frame, text=self.text, width=40)
        self.label_computer.grid(row=0, column=0)
        self.start_btn.grid(row=0, column=1, sticky="news")
        self.stats_btn.grid(row=0, column=2, sticky="news")
        self.back_to_btn.grid(row=0, column=3, sticky="news")


class TopLayer:
    """
    A class use to build the frames and the labels of the top window ( the window where the game is representing,
    all the players moves) ... Methods ------- __init__(self, top_frame): add_info(self, guessed_number,
    number_guess, number_bulls, number_hits)
    """

    def __init__(self, top_frame):
        """ The function is building TopLayer, constructor
            :parameters: self: the function gets self as a parameter
            top_frame: the top frame
            :returns: the function do not return any value
        """
        self.computer_layers = []
        self.top_frame = top_frame

    def create_computer_frames(self, number_of_computers):
        self.computer_layers = [ComputerLayer(
            tk.Frame(master=self.top_frame, borderwidth="2", relief=tk.RIDGE, height=200), i)
            for i in
            range(number_of_computers)]

    def add_info(self, layer, guessed_number, table_size, number_guess, number_bulls, number_hits):
        """ The function is adding information to the frame that show a move in the game (a guess of the player)
            :parameters: self: the function gets self as a parameter
            guessed_number: the number that the player is guessing
            number_guess: number of  guesses the player was trying to guess (including this)
            number_bulls: number of bulls in the guess
            number_hits: number of hits in the guess
            :returns: the function do not return any value
        """
        new_frame = tk.Frame(
            master=self.computer_layers[layer - 1].frame,
            relief=tk.RIDGE,
            borderwidth=2,
        )
        label_guess = tk.Label(master=new_frame,
                               text=f"Guess-{number_guess}:Number-{guessed_number}\n[Table Size:{table_size}]",
                               height=4)
        label_bh = tk.Label(master=new_frame, text=f"{number_bulls}", width=5)
        label_bn = tk.Label(master=new_frame, text=f"{number_hits}", justify="center", width=10)
        new_frame.pack(fill=tk.BOTH)
        for i in range(3):
            new_frame.columnconfigure(index=i, weight=1, minsize=5)
        label_guess.grid(row=0, column=0, sticky="w")
        label_bh.grid(row=0, column=1, sticky="e")
        label_bn.grid(row=0, column=2, sticky="e")


class BottomLayer:
    """
    A class use to build the frames and the labels of the bottom window
    ...
    Methods
    -------
    __init__(self, bottom_frame):
    
    """

    def __init__(self, bottom_frame):
        """ The function is building BottomLayer, constructor
            :parameters: self: the function gets self as a parameter
            top: the top frame
            bottom_frame: the bottom frame
            :returns: the function do not return any value
        """

        self.info_layer = InfoLayer(info_layer=bottom_frame, label=None, text="Start the game by pressing START =>")
        self.bottom_frame = bottom_frame


class MainWindow:
    """
    A class use to represent the main window of the game
    ...
    Methods
    -------
    __init__(self, top, bottom)
    top_window(self, number_1)
    bottom_window(self)
    """

    def __init__(self, top, bottom):
        """ The function is building MainWindow, constructor
            :parameters: self: the function gets self as a parameter
            top: the top frame
            bottom: the bottom frame
            :returns: the function do not return any value
        """

        self.top = TopLayer(top_frame=top)
        self.bottom = BottomLayer(bottom_frame=bottom)
        self.top.top_frame.pack(fill=tk.BOTH, expand=True)
        self.bottom.bottom_frame.pack(fill=tk.BOTH)

    def top_window(self):
        """ The function is building the top window where computer 1 and computer 2 game is displaying,
             where the game is represented, all the players moves
            :parameters: self: the function gets self as a parameter
            number_1: the random number (4 digits) you need to guess for the game
            :returns: the function do not return any value
        """

        # Computer 1
        for computer_layer in self.top.computer_layers:
            computer_layer.guess_number = ""
            computer_layer.frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
            computer_layer.computer_header_layer(25)
            computer_layer.playing_grid()

    def bottom_window(self):
        """ The function is building the bottom window of the main window
            :parameters: self: the function gets self as a parameter
            :returns: the function do not return any value
        """

        self.bottom.info_layer.info_grid()


def stats_and_game(game_window, stats_window):
    """ The function is hiding the statistics window and opening the game window
                :parameters: game_window: main game window
                stats_window: statistics window
                :returns: the function do not return any value
    """
    game_window.deiconify()
    stats_window.withdraw()


class DisplayGame:
    """
    A class use to set up the game display, the windows
    ...
    Attributes
    ----------
    window : create a main window
    
    Methods
    -------
    __init__(self)
    display(self, number_1)
    """

    number_of_digits = 0

    def __init__(self):
        """ The function building DisplayGame, constructor
            :parameters: self: the function gets self as a parameter
            :returns: the function do not return any value
        """

        self.window = tk.Tk()
        self.window.wm_attributes("-topmost", 1)
        self.window.title("Game Screen")
        self.window.withdraw()
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

    def display(self, number_of_computers):
        """ The function building the display of the game
        after we press the button of the start menu
        :parameters: self: the function gets self as a parameter
        number_1: the random number (4 digits) you need to guess for the game
        :returns: the function do not return any value
        """

        width = self.window.winfo_screenwidth()
        height = self.window.winfo_screenheight()
        self.window.geometry("%dx%d" % (width-100, height-100))
        self.main_window.top.create_computer_frames(number_of_computers=number_of_computers)
        self.main_window.top_window()
        self.main_window.bottom_window()
        self.window.mainloop()

    def restart_game(self):
        """ The function is restarting the game display
                :parameters: self: the function gets self as a parameter
                :returns: the function do not return any value
        """
        self.main_window.top.top_frame.destroy()
        self.main_window.top = TopLayer(top_frame=tk.Frame(
            master=self.window,
            height=100,
            border=1))
        self.main_window.top.top_frame.pack(fill=tk.BOTH, expand=True, side=tk.TOP)
        self.main_window.bottom.bottom_frame.pack(side=tk.BOTTOM)
        self.main_window.bottom.info_layer.label_computer.config(text="")


class StatsWindow:
    """
        A class use to represent the statistics window of the game,
        displays average guesses per game, number of wins for each computer,
        number of draws and number of games
        ...
        Methods
        -------
        def __init__(self)
        def computer_stats(self,data_base,number_of_computers,game_number)
        def create_header(self,game_number,number_of_digits, draws, games,zero)
        def init_frames(self,data_base)
        def callback(self,game_number,data_base)

    """
    def __init__(self):
        """ The function is building StatsWindow, constructor
                    :parameters: self: the function gets self as a parameter
                    :returns: the function do not return any value
        """
        self.window = tk.Tk()
        self.window.title("Stats")
        width = self.window.winfo_screenwidth()
        height = self.window.winfo_screenheight()
        self.window.geometry("%dx%d" % (width-100, height-100))
        self.window.wm_attributes("-topmost", 1)
        self.window.rowconfigure(0, minsize=800, weight=1)
        self.window.columnconfigure(1, minsize=800, weight=1)
        self.frame_1 = tk.Frame(master=self.window, border=2, relief=tk.RIDGE, width=100)
        self.frame_2 = tk.Frame(master=self.window, border=2, relief=tk.RIDGE, width=100)
        self.back_btn = tk.Button(master=self.frame_1, text="Back to Game",width=10,height=10)
        self.menu = tk.Listbox(master=self.frame_1,height=38)
        self.frame_list = []

    def computer_stats(self, data_base, number_of_computers, game_number):
        """ The function is updating the statistics of the latest game for each computer
            :parameters: self: the function gets self as a parameter
            data_base: where we store all the data for the statistics
            number_of_computers: number of players on the latest game
            game_number: the number of the latest game
            :returns: the function do not return any value
        """
        computer_list = data_base.games.get(f'Game {game_number+1}').get('Computers')
        computers_frame = tk.Frame(master=self.frame_2,border=2,relief=tk.RIDGE)
        computers_frame.pack(fill=tk.BOTH,expand=True)
        for number in range(number_of_computers):
            computers_frame.columnconfigure(number,minsize=10,weight=1)
        for rows in range(4):
            computers_frame.rowconfigure(rows,minsize=10,weight=1)
            for computer in range(number_of_computers):
                tk.Label(
                    master=computers_frame, relief=tk.RIDGE, border=1,
                    text=f"Computer Name: {computer+1}",
                    justify="center", font=f"BOLD {30}") \
                    .grid(row=0, column=computer, sticky="new")
                tk.Label(
                    master=computers_frame, relief=tk.RIDGE, border=1,
                    text=f"Computer Won: {computer_list[computer]['Won']}",
                    anchor="w",
                    font=f"BOLD {30}") \
                    .grid(row=1, column=computer, sticky="new")
                tk.Label(
                    master=computers_frame, relief=tk.RIDGE, border=1,
                    text=f"Computer Lost: {computer_list[computer]['Lost']}",
                    anchor="w",
                    font=f"BOLD {30}") \
                    .grid(row=2, column=computer, sticky="new")
                tk.Label(
                    master=computers_frame, relief=tk.RIDGE, border=1,
                    anchor="w",
                    text=f"Average guess:  {data_base.average_calculator(game_number=game_number,computer_number=computer)}"
                    , font=f"BOLD {30}") \
                    .grid(row=3, column=computer, sticky="new")

    def create_header(self, game_number, number_of_digits, draws, games, zero):
        """ The function is updating the statistics of the latest game for each computer
            :parameters: self: the function gets self as a parameter
            data_base: where we store all the data for the statistics
            number_of_computers: number of players on the latest game
            game_number: the number of the latest game
            :returns: the function do not return any value
        """

        header_frame = tk.Frame(master=self.frame_2, border=2, relief=tk.RIDGE,height=100,width=100)
        header_frame.pack(fill=tk.BOTH)
        top=tk.Frame(master=header_frame,
                 height=100,
                 width=100)
        top.pack(fill=tk.BOTH)
        top.columnconfigure([0, 1, 2], minsize=10, weight=1)
        bottom = tk.Frame(master=header_frame,
                 height=100,
                 width=100)
        bottom.pack(fill=tk.BOTH)
        bottom.columnconfigure([0, 1, 2,3],minsize =10, weight=1)
        tk.Label(
            master=top,
            relief=tk.RIDGE,
            border=1,
            text=f"Game Number: {game_number}",
            justify="center", font=f"BOLD {30}") \
            .grid(row=0, column=1,sticky="news")

        tk.Label(
            master=bottom,relief=tk.RIDGE,border=1,
            text=f"Number of Games: {games}",
            justify="center", font=f"BOLD {20}") \
            .grid(row=1,column=0,sticky="nsew")
        tk.Label(
            master=bottom,relief=tk.RIDGE,border=1,
            text=f"Number of Draws: {draws}",
            justify="center", font=f"BOLD {20}") \
            .grid(row=1, column=1,sticky="nsew")
        tk.Label(
            master=bottom,relief=tk.RIDGE,border=1,
            text=f"Number of Digits: {number_of_digits}",
            justify="center", font=f"BOLD {20}") \
            .grid(row=1, column=2,sticky="nsew")
        tk.Label(
            master=bottom, relief=tk.RIDGE, border=1,
            text=f"With Zero: {zero}",
            justify="center", font=f"BOLD {20}") \
            .grid(row=1, column=3, sticky="nsew")

    def init_frames(self, data_base):
        """ The function is initializing the frames
            :parameters: self: the function gets self as a parameter
            data_base: where we store all the data for the statistics
            :returns: the function do not return any value
        """
        self.frame_1.grid(row=0, column=0, sticky="ns")
        self.frame_2.grid(row=0, column=1, sticky="nsew")
        for i in range(2):
            self.frame_2.rowconfigure(i, weight=1, minsize=2)
        for game in range(data_base.number_of_games):
            tk.Button(master=self.frame_1, text=f"Game {game+1}", width=1, height=1,
                      command=lambda: self.callback(game_number=game, data_base=data_base))\
                .pack(fill=tk.BOTH)
        self.back_btn.pack(fill=tk.BOTH, side=tk.BOTTOM)

    def callback(self, game_number, data_base):
        """ The function is initializing the statistics, gets a calls when we press on callback button
                    :parameters: self: the function gets self as a parameter
                    data_base: where we store all the data for the statistics
                    :returns: the function do not return any value
        """
        if len(self.frame_list)>0:
            for frame in self.frame_list:
                frame.grid_forget()
                frame.destroy()
            self.frame_list = []
        if data_base.games[f'Game {game_number+1}']['Games Played'] > 0 :
            self.create_header(game_number=game_number+1,
                               number_of_digits=data_base.games[f'Game {game_number+1}']['Number of Digits'],
                               draws=data_base.games[f'Game {game_number+1}']['Draws'],
                               games=data_base.games[f'Game {game_number+1}']['Games Played'],
                               zero=data_base.games[f'Game {game_number+1}']['Zero']
                               )
            self.computer_stats(data_base=data_base,
                                number_of_computers=len(data_base.games[f'Game {game_number+1}']['Computers']),
                                game_number=game_number)
            for key in self.frame_2.children:
                self.frame_list.append(self.frame_2.children[key])
        else:
            self.window.wm_attributes("-topmost", 0)
            messagebox.showerror("showerror", "Error")
            self.window.wm_attributes("-topmost", 1)


def stats_open(data_base, window, thread):
    """ The function is opening the statistics window and hiding the ather windows
                        :parameters: self: the function gets self as a parameter
                        data_base: where we store all the data for the statistics
                        :returns: the function do not return any value
    """
    if len(thread) < 2:
        if data_base.number_of_games != 0:
            window.withdraw()
            stats = StatsWindow()
            stats.init_frames(data_base)
            stats.back_btn.config(command=lambda: stats_and_game(stats_window=stats.window, game_window=window))
            stats.window.mainloop()
    else:
        pass
