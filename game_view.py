"""The view of the main game window"""

import arcade
import key_controller
class GameView(arcade.View):

    def __init__(self):
        super().__init__()
        self.key_controller = key_controller.KeyController()



    def on_key_press(self, symbol, modifiers):
        movement = self.key_controller.get_movement(symbol)
        if movement is not None:
            player, direction = movement
            # Next line is a just and idea as we do  not have anything implemented yet
            self.game.handle_movement(player, direction)

    def on_draw(self):





