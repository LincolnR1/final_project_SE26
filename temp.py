"""UPDATED Testing file I had made while I write snake.py"""


import arcade
from snake import Snake

# Window configuration
WIDTH = 800
HEIGHT = 600
CELL_SIZE = 25

# Movement intervals (seconds per cell)
NORMAL_INTERVAL = 0.15
BOOST_INTERVAL = 0.075


class SnakeTest(arcade.Window):
    """Testing environment for snake functionality."""

    def __init__(self):
        super().__init__(WIDTH, HEIGHT, "Snake Testing")

        self.background_color = arcade.color.BLACK

        self.snake = Snake(
            start_position=(10, 10),
            direction=(1, 0),
            length=3
        )

        self.move_timer = 0.0

    def on_draw(self):
        """Draw the snake and boost energy bar."""
        self.clear()

        # Draw snake segments
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

    def on_key_press(self, key, modifiers):
        """Handle direction changes and boost activation."""

        directions = {
            arcade.key.UP: (0, 1),
            arcade.key.DOWN: (0, -1),
            arcade.key.LEFT: (-1, 0),
            arcade.key.RIGHT: (1, 0)
        }

        # Movement controls
        direction = directions.get(key)

        if direction is not None:
            self.snake.set_direction(direction)

        # Start boosting
        if key in (
            arcade.key.LSHIFT,
            arcade.key.RSHIFT
        ):
            self.snake.set_boosting(True)

    def on_key_release(self, key, modifiers):
        """Stop boosting when Shift is released."""

        if key in (
            arcade.key.LSHIFT,
            arcade.key.RSHIFT
        ):
            self.snake.set_boosting(False)


def main():
    """Start the snake testing window."""
    SnakeTest()
    arcade.run()


if __name__ == "__main__":
    main()

