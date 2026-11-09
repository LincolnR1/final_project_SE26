"""The view of the main game window"""
import random
import arcade
import key_controller
import snake
from col_and_round import Round
import consts

#Note to self, for camera, for the game to fit like we want it to:
# Window configuration
WIDTH = consts.WIDTH
HEIGHT = consts.HEIGHT
CELL_SIZE = consts.CELL_SIZE

# For spawning in objectives
GRID_COLS = WIDTH // CELL_SIZE
GRID_ROWS = HEIGHT // CELL_SIZE


class GameView(arcade.View):
    """The view of the main game window, loads in the objectives and movement"""
    def __init__(self):
        super().__init__()
        self.key_controller = key_controller.KeyController()
        # self.tile_map
        self.background_color = arcade.csscolor.LIGHT_GREEN
        self.tile_map = None
        #self.wall_list = arcade.SpriteList(use_spatial_hash=True,
        #                                   spatial_hash_cell_size=128)

        #creates snakes, no clue if the coords are what we want them to be or not yet though
        self.player_snake = snake.Snake(start_position=(5, 4), direction=(1, 0),
                                        length=3, color=arcade.csscolor.GREEN)
        self.enemy_snake = snake.Snake(start_position=(15, 4), direction=(-1, 0),
                                       color=arcade.csscolor.RED)
    # self.barrier_list = arcade.AStarBarrierList(self.enemy_snake,
        self.round = None
        self.scene = None


    def occupied_cells(self) -> set:
        """Basically goes through cells and keeps track of ones where the snake is,"""
        cells = set()
        for current_snake in (self.player_snake, self.enemy_snake):
            cells.update(current_snake.segments)
        return cells

    def spawn_objective(self) -> None:
        """Spawns the square in a random spot for which is not being occupied."""
        occupied = self.occupied_cells()
        free_cells = [(col, row)
                      for col in range(GRID_COLS)
                      for row in range(GRID_ROWS)
                      if (col, row) not in occupied]
        self.round.set_objective(random.choice(free_cells))

    def draw_objective(self) -> None:
        """Draws the objective square(the goal)"""
        if self.round.objective is None:
            return
        col, row = self.round.objective
        arcade.draw_lbwh_rectangle_filled(
            col * CELL_SIZE + 2, row * CELL_SIZE + 2,
            CELL_SIZE - 4, CELL_SIZE - 4,
            arcade.color.ELECTRIC_BLUE,
            )

    def check_objective(self) -> None:
        """Checks if the snake head has hit the objective."""
        for current_snake in (self.player_snake, self.enemy_snake):
            if current_snake.segments[0] == self.round.objective:
                self.spawn_objective()
                return

    def on_key_press(self, symbol, modifiers):
        """Controls keyboard input."""
        movement = self.key_controller.get_movement(symbol)
        if movement is not None:
            player, direction = movement

            if player == 1:
            # Next line is a just and idea as we do not have anything implemented yet
                self.handle_movement(player, direction)

    def handle_movement(self, player, direction):
        """handles snakes as far as what is what and who is who"""
        if player == 1:
            selected_snake = self.player_snake
        elif player == 2:
            selected_snake = self.enemy_snake
        else:
            return None
        # sets snake direction
        return selected_snake.set_direction(direction)

    def on_show_view(self):
        """Loads in all the snake games maps here"""
        layer_options = {
            "Walls": {"use_spatial_hash": True,
                      "scaling": 1.0},
            "Background": {"use_spatial_hash": False,
                           "scaling": 1.0},
            }
        self.tile_map = arcade.load_tilemap("maps/CS3050_final_project_level1.tmx",
                                            scaling=1, layer_options=layer_options)
        self.scene = arcade.Scene.from_tilemap(self.tile_map)
        

        wall_sprites = self.scene.get_sprite_list("Walls")

        self.round = Round(
            self.player_snake,
            self.enemy_snake,
            wall_sprites,
            objective=(12,8)
        )
        self.spawn_objective()
       # self.physics_engine = arcade.PhysicsEngineSimple(walls=self.scene["Walls"])

    def on_update(self, delta_time):
        """Update boost energy and snake movement."""
        self.round.update(delta_time)
        self.check_objective()

    def on_draw(self):
        """Render the screen."""
        self.clear()
        
        self.scene.draw()
        self.draw_objective()

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
