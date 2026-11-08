"""
Main file. Loads Arcade window and Game View (and eventually others) on top of it. 
"""
import arcade
import consts
from title_screen import TitleScreen

class SnakeGame(arcade.Window):
    """
    Main application class.
    """
    def __init__(self):
        # Call the parent class to set up the window
        super().__init__(consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT, consts.WINDOW_TITLE)

def main():
    """Main function"""
    window = arcade.Window(consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT, consts.WINDOW_TITLE, center_window=True)
    window.show_view(TitleScreen())
    arcade.run()

if __name__ == "__main__":
    main()