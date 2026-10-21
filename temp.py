"""Testing file I made while I write snake.py"""


import arcade
from snake import Snake

# Window settings
WIDTH = 1000
HEIGHT = 800
CELL_SIZE = 15

# Snake movement interval (seconds)
MOVE_INTERVAL = 0.15


class SnakeTest(arcade.Window):
    """Temporary window for testing the Snake class."""

    def __init__(self):
        super().__init__(WIDTH, HEIGHT, "Snake Testing")

        self.background_color = arcade.color.BLACK

        self.snake = Snake(
            start_position=(10, 10),
            direction=(1, 0),
            length=3
        )

        self.move_timer = 0

    def on_draw(self):
        """Draw the snake on the screen."""
        self.clear()

        for x, y in self.snake.segments:
            arcade.draw_lbwh_rectangle_filled(
                x * CELL_SIZE,
                y * CELL_SIZE,
                CELL_SIZE - 1,
                CELL_SIZE - 1,
                arcade.color.GREEN
            )

    def on_update(self, delta_time):
        """Move the snake at a fixed interval."""
        self.move_timer += delta_time

        if self.move_timer >= MOVE_INTERVAL:
            self.move_timer -= MOVE_INTERVAL

            # Temporary movement logic
            head_x, head_y = self.snake.segments[0]
            dx, dy = self.snake.direction

            new_head = (
                (head_x + dx) % (WIDTH // CELL_SIZE),
                (head_y + dy) % (HEIGHT // CELL_SIZE)
            )

            self.snake.segments.insert(0, new_head)
            self.snake.segments.pop()

    def on_key_press(self, key, modifiers):
        """Change the snake's direction."""
        directions = {
            arcade.key.UP: (0, 1),
            arcade.key.DOWN: (0, -1),
            arcade.key.LEFT: (-1, 0),
            arcade.key.RIGHT: (1, 0)
        }

        new_direction = directions.get(key)

        if new_direction is not None:
            dx, dy = self.snake.direction

            # Prevent reversing directly into the body
            if new_direction != (-dx, -dy):
                self.snake.direction = new_direction


def main():
    SnakeTest()
    arcade.run()


if __name__ == "__main__":
    main()
