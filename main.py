import main_game
import start_screen
import bulls_and_hits as bh

first_window = start_screen.StartScreen()
game_backend = bh.BH()

display = main_game.DisplayGame()

game_backend.create_list()
game_backend.choose_random()
start_number = game_backend.start_number
final_bulls = game_backend.number_of_digits
print("first")

def change_window():
    first_window.destroy_window()
    display.display(number_1=start_number)


def game_loop():
    counter = 0
    while game_backend.number_bulls != game_backend.number_of_digits:
        game_backend.temp_number = game_backend.start_number
        counter = counter + 1
        game_backend.create_guess()
        game_backend.find_bulls_hits()
        display.main_window.top.add_info(
            number_bulls=game_backend.number_bulls,
            number_hits=game_backend.number_hits,
            number_guess=counter,
            guessed_number=game_backend.guess
        )
        game_backend.temp_number = game_backend.guess
        game_backend.nh = game_backend.number_hits
        game_backend.nb = game_backend.number_bulls
        game_backend.reduce_table()


display.main_window.bottom.info_layer.btn.config(command=game_loop)
first_window.start_btn.config(command=change_window)
first_window.create_start()
