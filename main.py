import main_game
import start_screen
import bulls_and_hits as bh
import threading as thread
import time

first_window = start_screen.StartScreen()

display = main_game.DisplayGame()


def change_window():
    first_window.destroy_window()
    display.display()


def start_game_loops():
    t_1.start()
    t_2.start()


def game_loop(number):
    lock = thread.Lock()
    game_backend = bh.BH()
    game_backend.create_list()
    game_backend.choose_random()
    start_number = game_backend.start_number
    if number == 1:
        display.main_window.top.computer_1_layer.number_label.configure(text=f"The number is: {start_number}")
    if number == 2:
        display.main_window.top.computer_2_layer.number_label.configure(text=f"The number is: {start_number}")
    counter = 0
    lock.acquire()
    if number == 1:
        data_base_1.add_game(
            number=game_backend.start_number,
            game_number=counter + 1,
            table_size=len(game_backend.number_list))
    if number == 2:
        data_base_2.add_game(
            number=game_backend.start_number,
            game_number=counter + 1,
            table_size=len(game_backend.number_list))
    lock.release()
    while game_backend.number_bulls != game_backend.number_of_digits or t_1.is_alive() or t_2.is_alive():
        lock.acquire()
        game_backend.temp_number = game_backend.start_number
        counter = counter + 1
        game_backend.create_guess()
        if number == 1:
            data_base_1.games.get(f"Game {data_base_1.number_of_games}")["guess"].append(game_backend.guess)
        if number == 2:
            data_base_2.games.get(f"Game {data_base_2.number_of_games}")["guess"].append(game_backend.guess)
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
        game_backend.temp_number = game_backend.guess
        game_backend.nh = game_backend.number_hits
        game_backend.nb = game_backend.number_bulls
        game_backend.reduce_table()
        if number == 1:
            data_base_1.games.get(f"Game {data_base_1.number_of_games}")["table size"].append(
                len(game_backend.number_list))
        if number == 2:
            data_base_2.games.get(f"Game {data_base_2.number_of_games}")["table size"].append(
                len(game_backend.number_list))
        lock.release()


t_1 = thread.Thread(target=game_loop, args=[1])
t_2 = thread.Thread(target=game_loop, args=[2])
data_base_1 = bh.BullsHitsDB(player=1)
data_base_2 = bh.BullsHitsDB(player=2)

display.main_window.bottom.info_layer.btn.config(command=start_game_loops)  # Start button on Display Game
first_window.start_btn.config(command=change_window)
first_window.create_start()  # First window to showcase game
