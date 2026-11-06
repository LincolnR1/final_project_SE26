"""The view of the main game window"""

import arcade
import key_controller
import snake
from col_and_round import Round

#Note to self, for camera, for the game to fit like we want it to:
#width should be 960 and height is 720
# Constants
# WINDOW_WIDTH = 960
# WINDOW_HEIGHT = 720
# WINDOW_TITLE = "Cracked_Snake"
# Window configuration
WIDTH = 800
HEIGHT = 600
#CELL_SIZE = 25

# Movement intervals (seconds per cell)
NORMAL_INTERVAL = 0.15
BOOST_INTERVAL = 0.075

class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.key_controller = key_controller.KeyController()
        # self.tile_map
        self.background_color = arcade.csscolor.CORNFLOWER_BLUE
        self.tile_map = None


        #creates snakes, no clue if the coords are what we want them to be or not yet though
        self.player_snake = snake.Snake(
            start_position=(5, 4),
            direction=(1, 0),
            length=3
        )

        self.enemy_snake = snake.Snake(
            start_position=(15, 4),
            direction=(-1, 0),
            length=3
        )  

        self.round = None    
        self.move_timer = 0.0
        self.scene = None


    def on_key_press(self, symbol, modifiers):
        movement = self.key_controller.get_movement(symbol)
        if movement is not None:
            player, direction = movement
            # Next line is a just and idea as we do  not have anything implemented yet
            self.handle_movement(player, direction)

    def on_update(self, delta_time):
        """Forward arcade updates to current round"""
        self.round.update(delta_time)

    def handle_movement(self, player, direction):
        # handles snakes as far as what is what and who is who
        if player == 1:
            selected_snake = self.player_snake
        elif player == 2:
            selected_snake = self.enemy_snake
        else:
            return None

        return selected_snake.set_direction(direction)

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
        
        wall_sprites = self.scene.get_sprite_list("Walls")

        self.round = Round(
            self.player_snake,
            self.enemy_snake,
            wall_sprites
        )

    def on_draw(self):
        """Render the screen."""
        self.clear()
        
        self.scene.draw()

        self.round.snake_visuals[1].sprites.draw()
        self.round.snake_visuals[2].sprites.draw()

        ##TODO: add boost functionality, code commented out for now
        #     # Draw boost energy bar background
        # arcade.draw_lbwh_rectangle_filled(
        #     20, HEIGHT - 40,
        #     200, 20,
        #     arcade.color.DARK_GRAY
        # )

        
        # Draw current boost energy
        # energy_ratio = (
        #         self.snake.boost_energy /
        #         self.snake.max_boost_energy
        # )
       
        # arcade.draw_lbwh_rectangle_filled(
        #     20, HEIGHT - 40,
        #         200 * energy_ratio, 20,
        #     arcade.color.YELLOW
        # )

        # arcade.draw_text(
        #     "BOOST (Hold Shift)",
        #     20, HEIGHT - 60,
        #     arcade.color.WHITE,
        #     12
        # )

        # Display boost status
        # status = (
        #     "BOOSTING"
        #     if self.snake.is_boosting
        #     else "NORMAL"
        # )

        # arcade.draw_text(
        #     f"Speed: {status}",
        #     20, HEIGHT - 85,
        #     arcade.color.WHITE,
        #     12
        # )







