import arcade
from arcade.examples.camera_platform import TILE_SCALING

#Note to self, for camera, for the game to fit like we want it to:
#width should be 960 and height is 720
# Constants
WINDOW_WIDTH = 960  
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Cracked_Snake"

class SnakeGame(arcade.Window):
    def __init__(self):
        # Call the parent class to set up the window
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE, center_window=True)
        # self.tile_map
        self.background_color = arcade.csscolor.CORNFLOWER_BLUE
        self.tile_map = None

        self.camera = None

        self.scene = None

    def setup(self):
        """
        We load all the snake games maps here
        """
        layer_options = {
            "Walls": {"use_spatial_hash": True,
                      "scaling": 1.0},
            "Background": {"use_spatial_hash": False,
                           "scaling": 1.0},
            }
        self.camera = arcade.Camera2D()
        self.tile_map = arcade.load_tilemap("maps/CS3050_final_project_level1.tmx",
                                            scaling=1, layer_options=layer_options)
        self.scene = arcade.Scene.from_tilemap(self.tile_map)
       # self.physics_engine = arcade.PhysicsEngineSimple(walls=self.scene["Walls"])

    def update(self):
        self.physics_engine.update()

    def on_draw(self):
        """Render the screen."""
        self.clear()
        self.camera.use()
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
