"""The view of the main game window"""

import arcade
import key_controller
import snake
from maps import Maps

#Note to self, for camera, for the game to fit like we want it to:
#width should be 960 and height is 720
# Constants
# WINDOW_WIDTH = 960
# WINDOW_HEIGHT = 720
# WINDOW_TITLE = "Cracked_Snake"

class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.key_controller = key_controller.KeyController()
        # self.tile_map
        self.background_color = arcade.csscolor.CORNFLOWER_BLUE
        self.tile_map = None

        #creates snakes, no clue if the coords are what we want them to be or not yet though
        self.snake1 = snake.Snake(start_position=(5, 4))
        self.snake2 = snake.Snake(start_position=(15, 4), direction=(-1, 0))

        self.scene = None

    def on_key_press(self, symbol, modifiers):
        movement = self.key_controller.get_movement(symbol)
        if movement is not None:
            player, direction = movement
            # Next line is a just and idea as we do  not have anything implemented yet
            self.handle_movement(player, direction)

    def handle_movement(self, player, direction):
        # handles snakes as far as what is what and who is who
        if player == 1:
            snake = self.snake1
        elif player == 2:
            snake = self.snake2
        else:
            return None
        # sets snake direction
        snake.direction = direction

        # tells snake where to move
        new_x = snake.segments[0][0] + snake.direction[0]
        new_y = snake.segments[0][1] + snake.direction[1]
        snake.segments.insert(0, (new_x, new_y))
        snake.segments.pop()

    def on_show_view(self):
        """
        We load all the snake games maps here
        """
        layer_options = {
            "Walls": {"use_spatial_hash": True,
                      "scaling": 1.0},
            "Background": {"use_spatial_hash": False,
                           "scaling": 1.0},
            }
        self.tile_map = arcade.load_tilemap("maps/CS3050_final_project_level1.tmx",
                                            scaling=1, layer_options=layer_options)
        self.scene = arcade.Scene.from_tilemap(self.tile_map)
       # self.physics_engine = arcade.PhysicsEngineSimple(walls=self.scene["Walls"])

    def on_draw(self):
        """Render the screen."""
        self.clear()
        self.scene.draw()







