"""The view of the main game window"""

import arcade
import key_controller
import snake
import maps
class GameView(arcade.View):

    def __init__(self):
        super().__init__()
        self.key_controller = key_controller.KeyController()

        #creates snakes, no clue if the coords are what we want them to be or not yet though
        self.snake1 = snake.Snake(start_position=(5, 4))
        self.snake2 = snake.Snake(start_position=(15, 4), direction=(-1, 0))

        #attempting to load the map
        self.tile_map = None
        self.scene = None

    def on_key_press(self, symbol, modifiers):
        movement = self.key_controller.get_movement(symbol)
        if movement is not None:
            player, direction = movement
            # Next line is a just and idea as we do  not have anything implemented yet
            self.game.handle_movement(player, direction)

    def handle_movement(self, player, direction):
        # handles snakes as far as what is what and who is who
        if player == 1:
            snake = self.snake1


        elif player == 2:
            snake = self.snake2

        else:
            return

        # sets snake direction
        snake.direction = direction

        # tells snake where to move
        new_x = snake.segments[0][0] + snake.direction[0]
        new_y = snake.segments[0][1] + snake.direction[1]
        snake.segments.insert(0, (new_x, new_y))
        snake.segments.pop()

    def on_draw(self):



