from functools import reduce

import main_game
import start_screen
import bulls_and_hits as bh
import threading as thread
import time


def change_window():
    first_window.destroy_window()
    display.display()


def game_loop(number, data_base):
    lock = thread.Lock()
    game_backend = bh.BH()
    game_backend.create_list()
    game_backend.choose_random()
    start_number = game_backend.start_number
    if number == 1:
        display.main_window.top.computer_1_layer.number_label.configure(text=f"The number is: {start_number}")
    if number == 2:
        display.main_window.top.computer_2_layer.number_label.configure(text=f"The number is: {start_number}")
    lock.acquire()
    data_base.add_game(
        number=game_backend.start_number,
        table_size=len(game_backend.number_list))
    lock.release()
    counter = 1
    while True:
        lock.acquire()
        game_backend.temp_number = game_backend.start_number
        game_backend.create_guess()
        data_base.games.get(f"Game {data_base.number_of_games - 1}")["guess"].append(game_backend.guess)
        game_backend.find_bulls_hits()
        display.main_window.top.add_info(
            layer=number,
            number_bulls=game_backend.number_bulls,
            number_hits=game_backend.number_hits,
            number_guess=counter,
            guessed_number=game_backend.guess
        )
        if game_backend.number_bulls == game_backend.number_of_digits:
            break
        counter += 1
        game_backend.temp_number = game_backend.guess
        game_backend.nh = game_backend.number_hits
        game_backend.nb = game_backend.number_bulls
        game_backend.reduce_table()
        data_base.games.get(f"Game {data_base.number_of_games - 1}")["table size"].append(
            len(game_backend.number_list))
        lock.release()


"""""""""
this function is to destroy the windows after the game is finished 
display.main_window.top.computer_1_layer.frame.winfo_children()[2].destroy()
display.main_window.top.computer_2_layer.frame.winfo_children()[2].destroy()

"""


def restart_windows(array):
    for i, frame in filter(lambda x: x[0] >= 2, enumerate(array)):
        frame.destroy()


def start_game_loops():
    if data_base_1.number_of_games >= 1:
        restart_windows(display.main_window.top.computer_1_layer.frame.winfo_children())
        restart_windows(display.main_window.top.computer_2_layer.frame.winfo_children())
        data_base_1.number_of_games += 1
        data_base_2.number_of_games += 1
        thread.Thread(target=game_loop, args=[1, data_base_1]).start()
        thread.Thread(target=game_loop, args=[2, data_base_2]).start()
    else:
        data_base_1.number_of_games += 1
        data_base_2.number_of_games += 1
        t_1.start()
        t_2.start()


first_window = start_screen.StartScreen()
data_base_1 = bh.BullsHitsDB(player=1)
data_base_2 = bh.BullsHitsDB(player=2)
t_1 = thread.Thread(target=game_loop, args=[1, data_base_1])
t_2 = thread.Thread(target=game_loop, args=[2, data_base_2])
display = main_game.DisplayGame()
display.main_window.bottom.info_layer.btn.config(command=start_game_loops)  # Start button on Display Game
first_window.start_btn.config(command=change_window)
first_window.create_start()  # First window to showcase game
