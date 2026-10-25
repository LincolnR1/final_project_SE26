"""
Main file. Loads Arcade window and Game View (and eventually others) on top of it. 
"""
import arcade
from game_view import GameView

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
        # self.tile_map
        self.background_color = arcade.csscolor.CORNFLOWER_BLUE

def main():
    """Main function"""
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, "Cracked Snake Game", center_window=True)
    menu_view = GameView()
    window.show_view(menu_view)
    arcade.run()

if __name__ == "__main__":
    main()