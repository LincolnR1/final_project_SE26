"""The view of the main game window"""

import arcade
import key_controller
import snake
import random
from col_and_round import Round
import consts

#Note to self, for camera, for the game to fit like we want it to:

# Window configuration
WIDTH = consts.WIDTH
HEIGHT = consts.HEIGHT
CELL_SIZE = consts.CELL_SIZE

# Movement intervals (seconds per cell)
NORMAL_INTERVAL = consts.NORMAL_INTERVAL
BOOST_INTERVAL = consts.BOOST_INTERVAL

# For spawning in objectives
GRID_COLS = WIDTH // CELL_SIZE
GRID_ROWS = HEIGHT // CELL_SIZE


class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.key_controller = key_controller.KeyController()
        # self.tile_map
        self.background_color = arcade.csscolor.LIGHT_GREEN
        self.tile_map = None

       #self.wall_list = arcade.SpriteList(use_spatial_hash=True,
        #                                   spatial_hash_cell_size=128)



        #creates snakes, no clue if the coords are what we want them to be or not yet though
        #created enemy snake 11/1 TW
        self.player_snake = snake.Snake(start_position=(5, 4), direction=(1, 0), length=3, color=arcade.csscolor.GREEN)
        self.enemy_snake = snake.Snake(start_position=(15, 4), direction=(-1, 0), color=arcade.csscolor.RED)

   #     self.barrier_list = arcade.AStarBarrierList(self.enemy_snake, self.wall_list, CELL_SIZE,0,0,1280, 720)
        self.round = None
        self.move_timer = 0.0
        self.scene = None

        self.objective = None


    # Basically goes through cells and keeps track of ones where the snake is, etc, need to add walls and obstacles to this
    def occupied_cells(self) -> set:
        cells = set()
        for current_snake in (self.player_snake, self.enemy_snake):
            cells.update(current_snake.segments)
        return cells

    # Spawns the square in a random spot for which is not being occupied
    def spawn_objective(self) -> None:
        occupied = self.occupied_cells()
        free_cells = [(col, row)
                      for col in range(GRID_COLS)
                      for row in range(GRID_ROWS)
                      if (col, row) not in occupied]
        self.objective = random.choice(free_cells)

    # Draws the objective rectangle
    def draw_objective(self) -> None:
        if self.objective is None:
            return
        col, row = self.objective
        arcade.draw_lbwh_rectangle_filled(
            col * CELL_SIZE + 2, row * CELL_SIZE + 2,
            CELL_SIZE - 4, CELL_SIZE - 4,
            arcade.color.ELECTRIC_BLUE,
            )

    # checks of the snake head hit the objective
    def check_objective(self) -> None:
        for current_snake in (self.player_snake, self.enemy_snake):
            if current_snake.segments[0] == self.objective:
                self.spawn_objective()
                return

    def on_key_press(self, symbol, modifiers):
        movement = self.key_controller.get_movement(symbol)
        if movement is not None:
            player, direction = movement

            if player == 1:
            # Next line is a just and idea as we do  not have anything implemented yet
                self.handle_movement(player, direction)

    def update_enemy_direction(self):

        #
        if self.objective is None:
            return

        # Looks at enemy snakes current coordinates and compares them to
        # the objectives coordinates and adjusts the coordinates based on them
        enemy_x, enemy_y = self.enemy_snake.segments[0]
        target_x, target_y = self.objective

        if target_x > enemy_x:
            direction = (1, 0)

        elif target_y > enemy_y:
            direction = (0, 1)

        elif target_y < enemy_y:
            direction = (0, -1)

        elif target_x < enemy_x:
            direction = (-1, 0)
        else:
            return

        self.handle_movement(2, direction)



   


    def handle_movement(self, player, direction):
        # handles snakes as far as what is what and who is who
        if player == 1:
            selected_snake = self.player_snake
        elif player == 2:
            selected_snake = self.enemy_snake
        else:
            return None
        # sets snake direction
        return selected_snake.set_direction(direction)

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
        self.spawn_objective()

        wall_sprites = self.scene.get_sprite_list("Walls")

        self.round = Round(
            self.player_snake,
            self.enemy_snake,
            wall_sprites
        )
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







