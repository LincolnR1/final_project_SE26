"""
Main file. Loads Arcade window and Game View (and eventually others) on top of it. 
"""
import arcade
from title_screen import Title_Screen


# Constants
WINDOW_WIDTH = 960
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Cracked Snake Game"


class SnakeGame(arcade.Window):
    """
    Main application class.
    """
    def __init__(self):
        # Call the parent class to set up the window
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

def main():
    """Main function"""
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, "Cracked Snake Game", center_window=True)
    window.show_view(Title_Screen())
    arcade.run()

if __name__ == "__main__":
    main()