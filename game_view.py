"""The view of the main game window"""

import arcade
import key_controller
import snake

#Note to self, for camera, for the game to fit like we want it to:
#width should be 960 and height is 720
# Constants
# WINDOW_WIDTH = 960
# WINDOW_HEIGHT = 720
# WINDOW_TITLE = "Cracked_Snake"
# Window configuration
WIDTH = 800
HEIGHT = 600
CELL_SIZE = 25

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
        self.snake = snake.Snake(start_position=(5, 4), direction=(1, 0), length=3)
       # self.snake2 = Snake(start_position=(15, 4), direction=(-1, 0))
        self.move_timer = 0.0
        self.scene = None

    def on_key_press(self, symbol, modifiers):
        movement = self.key_controller.get_movement(symbol)
        if movement is not None:
            player, direction = movement
            # Next line is a just and idea as we do  not have anything implemented yet
            self.handle_movement(player, direction)

    def on_update(self, delta_time):
        """Update boost energy and snake movement."""
        # Update boost state and energy
        self.snake.update_boost(delta_time)

        # Determine movement speed
        if self.snake.is_boosting:
            interval = BOOST_INTERVAL
        else:
            interval = NORMAL_INTERVAL

        # Accumulate movement time
        self.move_timer += delta_time

        # Move when the timer reaches the interval
        while self.move_timer >= interval:

            self.snake.move()

            # Temporary wraparound for testing
            cols = WIDTH // CELL_SIZE
            rows = HEIGHT // CELL_SIZE

            self.snake.segments = [
                (x % cols, y % rows)
                for x, y in self.snake.segments
            ]
            self.move_timer -= interval

    def handle_movement(self, player, direction):
        # handles snakes as far as what is what and who is who
        if player == 1:
            snake = self.snake
     #   elif player == 2:
     #       snake = self.snake2
        else:
            return None
        # sets snake direction
        snake.direction = direction

        # tells snake where to move
        # new_x = snake.segments[0][0] + snake.direction[0]
        # new_y = snake.segments[0][1] + snake.direction[1]
        # snake.segments.insert(0, (new_x, new_y))
        # snake.segments.pop()

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
        for index, (x, y) in enumerate(self.snake.segments):
            color = (
                arcade.color.LIME_GREEN
                if index == 0
                else arcade.color.GREEN
            )

            arcade.draw_lbwh_rectangle_filled(
                x * CELL_SIZE,
                y * CELL_SIZE,
                CELL_SIZE - 1,
                CELL_SIZE - 1,
                color
            )

            # Draw boost energy bar background
        arcade.draw_lbwh_rectangle_filled(
            20, HEIGHT - 40,
            200, 20,
            arcade.color.DARK_GRAY
        )

        # Draw current boost energy
        energy_ratio = (
                self.snake.boost_energy /
                self.snake.max_boost_energy
        )

        arcade.draw_lbwh_rectangle_filled(
            20, HEIGHT - 40,
                200 * energy_ratio, 20,
            arcade.color.YELLOW
        )

        arcade.draw_text(
            "BOOST (Hold Shift)",
            20, HEIGHT - 60,
            arcade.color.WHITE,
            12
        )

        # Display boost status
        status = (
            "BOOSTING"
            if self.snake.is_boosting
            else "NORMAL"
        )

        arcade.draw_text(
            f"Speed: {status}",
            20, HEIGHT - 85,
            arcade.color.WHITE,
            12
        )







