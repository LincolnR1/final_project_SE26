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

        arcade.draw_text("CRACKED SNAKE", w / 2, h * 0.72,
                         (120, 255, 150), 60, anchor_x="center", bold=True)

        # Draw the player vs AI Button
        arcade.draw_lbwh_rectangle_outline(
            left=w/2 -210,
            bottom=h * 0.49 - 42.5,
            width=420,
            height=85,
            color=(20, 65, 40),
            border_width = 2
        )
        arcade.draw_text("PLAYER vs AI", w/2, h * 0.49 , (255, 255, 255), 28, anchor_x="center",anchor_y ="center", bold=False)

        arcade.draw_lbwh_rectangle_outline(
            left=w/2 - 210,
            bottom=h * 0.33 - 42.5 ,
            width=420,
            height= 85,
            color=(20, 65, 40),
            border_width = 2
        )
        arcade.draw_text("PLAYER vs PLAYER", w/2, h * 0.33, (255, 255, 255), 28, anchor_x="center",anchor_y ="center", bold=False)
        # Makes pulsing text which I thought was pretty cool
        alpha = int(160 + 95 * math.sin(self.time * 3))
        arcade.draw_text("Click a game mode to start", w / 2, h * 0.20,
                         (255, 255, 255, alpha), 20, anchor_x="center")



    # Both load into gameview if mouse is pressed or space bar is presssed
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int) -> None:
        "This will transition to the game screen."
        w, h = self.window.width, self.window.height
        if (w / 2 - 210 <= x <= w / 2 + 210 and
                h * 0.49 - 42.5 <= y <= h * 0.49 + 42.5):
            self.window.show_view(GameView("vs_ai"))

        elif (w / 2 - 210 <= x <= w / 2 + 210 and
                h * 0.33 - 42.5 <= y <= h * 0.33 + 42.5):
            self.window.show_view(GameView("2_player"))



    # def on_key_press(self, symbol, modifiers) -> None:
    #     if symbol in (arcade.key.SPACE, arcade.key.ENTER):
    #         self.window.show_view(GameView())
    #     elif symbol == arcade.key.ESCAPE:
    #         arcade.exit()
