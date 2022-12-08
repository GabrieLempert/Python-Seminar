import main_game
import start_screen
import bulls_and_hits as bh
import threading as thread
import time

from bulls_and_hits import BH


def change_window(zero):
    data_base.create_game(number_of_digits=first_window.number_of_digits.curselection()[0] + 4,zero=zero)
    if len(first_window.number_of_digits.curselection()) != 0:
        display.number_of_digits = first_window.number_of_digits.curselection()[0] + 4
    for i in range(int(first_window.number_of_computers.get())):
        data_base.games[f"Game {data_base.number_of_games}"]["Computers"].append(data_base.add_computer())
    number = int(first_window.number_of_computers.get())
    first_window.destroy_window()
    display.window.deiconify()
    display.display(number_of_computers=number)


def back_to_main():
    display.restart_game()
    display.window.withdraw()
    first_window.window.deiconify()


def game_logs():
    if len(thread.enumerate()) <= 2:
        display.main_window.bottom.info_layer.start_btn["state"] = "normal"
        display.main_window.bottom.info_layer.back_to_btn["state"] = "normal"
        display.main_window.bottom.info_layer.stats_btn["state"] = "normal"
        number_of_games = f"We played #{data_base.number_of_games} games"
        text=data_base.get_winner_loser()
        display.main_window.bottom.info_layer.label_computer.configure(text=f"{text}\n" + number_of_games)
    else:
        pass


def game_loop(number, number_of_digits):
    lock = thread.Lock()
    zero = data_base.games[f"Game {data_base.number_of_games}"]['Zero']
    game_backend: BH = bh.BH(number_of_digits=number_of_digits,zero=zero)
    game_backend.create_list()
    game_backend.choose_random()
    start_number = game_backend.start_number
    display.main_window.top.computer_layers[number - 1].number_label.configure(text=f"The number is: {start_number}")
    lock.acquire()
    data_base.add_game(
        computer_number=number-1,
        number=game_backend.start_number,
        table_size=len(game_backend.number_list))
    game_number = data_base.games[f'Game {data_base.number_of_games}']['Games Played']
    lock.release()
    counter = 1
    while True:
        lock.acquire()
        game_backend.temp_number = game_backend.start_number
        game_backend.create_guess()
        data_base.games.get(f'Game {data_base.number_of_games}').get('Computers')[number-1]['Games'][f'{game_number}']\
            ['guess'].append(game_backend.guess)
        game_backend.find_bulls_hits()
        display.main_window.top.add_info(
            table_size=len(game_backend.number_list),
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
        data_base.games.get(f"Game {data_base.number_of_games}").get("Computers")[number-1]['Games'][f'{game_number}']\
            ["table size"].append(len(game_backend.number_list))
        lock.release()
        time.sleep(0.95)
    game_logs()


# Restarts the window for new game
def restart_windows(array):
    [frame.destroy() for i, frame in filter(lambda x: x[0] >= 2, enumerate(array))]


#
def start_game_loops():
    data_base.games[f"Game {data_base.number_of_games}"]['Games Played'] += 1
    if data_base.number_of_games >= 1:
        for layer in display.main_window.top.computer_layers:
            restart_windows(layer.frame.winfo_children())
    if len(thread.enumerate()) < 2:
        for number in range(int(first_window.number_of_computers.get())):
            thread.Thread(target=game_loop, args=[number+1, int(display.number_of_digits)]).start()
        display.main_window.bottom.info_layer.start_btn["state"] = "disabled"
        display.main_window.bottom.info_layer.back_to_btn["state"] = "disabled"
        display.main_window.bottom.info_layer.stats_btn["state"] = "disabled"

def close_all():
    display.window.destroy()
    first_window.window.destroy()


if __name__ == "__main__":
    first_window = start_screen.StartScreen()
    data_base = bh.BullsHitsDB()
    display = main_game.DisplayGame()
    stats = main_game.StatsWindow
    display.main_window.bottom.info_layer.stats_btn.config(command=lambda: main_game.stats_open(
        data_base=data_base,
        window=display.window,
        thread=thread.enumerate()))
    display.main_window.bottom.info_layer.start_btn.config(command=start_game_loops)  # Start button on Display Game
    first_window.start_btn_zero.config(command=lambda :change_window(zero=True))
    first_window.start_btn_no_zero.config(command=lambda :change_window(zero=False))
    display.main_window.bottom.info_layer.back_to_btn.config(command=back_to_main)
    first_window.window.protocol("WM_DELETE_WINDOW", close_all)
    display.window.protocol("WM_DELETE_WINDOW", close_all)
    first_window.create_start()  # First window to showcase game
