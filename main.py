import main_game
import start_screen

first_window = start_screen.start()


def change_window():
    first_window.destroy_window()
    main_game.main()


first_window.start_btn.config(command=change_window)

first_window.create_start()
