import arcade
from arcade.examples.camera_platform import TILE_SCALING

# Constants
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Cracked_Snake"


class SnakeGame(arcade.Window):


    def __init__(self):

        # Call the parent class to set up the window
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
        # self.tile_map
        self.background_color = arcade.csscolor.CORNFLOWER_BLUE

        self.scene = None

    def setup(self):
        """
        We load all the snake games maps here
        """
        layer_options = {
            "Walls": {"use_spatial_hash": True},
            }
        self.tile_map = arcade.load_tilemap("maps/CS3050_final_project_level1.tmx",
                                            scaling=1.1,layer_options=layer_options)
        self.scene = arcade.Scene.from_tilemap(self.tile_map)


    def on_draw(self):
        """Render the screen."""
        self.clear()

        self.scene.draw()
        # The clear method should always be called at the start of on_draw.
        # It clears the whole screen to whatever the background color is
        # set to. This ensures that you have a clean slate for drawing each
        # frame of the game.
        # Code to draw other things will go here


def main():
    """Main function"""
    window = SnakeGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
