"""Title screen of the game"""
import math
import arcade
from game_view import GameView
class TitleScreen(arcade.View):
    """Title screen of the game, then transitions to the game screen."""
    def __init__(self):
        super().__init__()
        self.time = 0.0
    def on_show_view(self) -> None:
        "This shows the title screen"
        self.background_color = (10, 20, 15)

    def on_update(self, delta_time: float) -> None:
        self.time += delta_time

    def on_draw(self) -> None:
        "This should render the screen."
        self.clear()
        self.clear()
        w, h = self.window.width, self.window.height

        arcade.draw_text("CRACKED SNAKE", w / 2, h * 0.58,
                         (120, 255, 150), 52, anchor_x="center", bold=True)

        # Makes pulsing text which I thought was pretty cool
        alpha = int(160 + 95 * math.sin(self.time * 3))
        arcade.draw_text("Click or press SPACE to start", w / 2, h * 0.42,
                         (255, 255, 255, alpha), 20, anchor_x="center")



    # Both load into gameview if mouse is pressed or space bar is presssed
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int) -> None:
        "This will transition to the game screen."
        self.window.show_view(GameView())

    def on_key_press(self, symbol, modifiers) -> None:
        if symbol in (arcade.key.SPACE, arcade.key.ENTER):
            self.window.show_view(GameView())
        elif symbol == arcade.key.ESCAPE:
            arcade.exit()
