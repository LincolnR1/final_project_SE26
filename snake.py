"""Controls snake position and state (collision, length, boost, etc)"""

class Snake:
    """Represents a snake on the grid"""

    def __init__(self, start_position, direction=(1,0), length=3):
        self.direction = direction
        self.next_direction = direction
        self.segments = []

        #boost settings 
        self.max_boost_energy = 100.0
        self.boost_energy = self.max_boost_energy

        self.boost_drain_rate = 30.0 #can be fixed later with testing
        self.boost_regen_rate = 15.0

        self.is_boosting = False

        for i in range(length):
            x = start_position[0] - i * direction[0]
            y = start_position[1] - i * direction[1]

            self.segments.append((x,y))

        self.pending_growth = 0

    def move(self):
        """Advance the snake one grid cell."""
        #apply next direction
        self.direction = self.next_direction

        head_x, head_y = self.segments[0]

        dx, dy = self.direction

        new_head = (head_x + dx, head_y + dy)

        self.segments.insert(0, new_head)

        self.segments.pop()

        return new_head

    def set_direction(self, new_direction):
        """Set up a valid direction change."""

        valid_directions = {
            (0, 1),
            (0, -1),
            (-1, 0),
            (1, 0)
        }

        if new_direction not in valid_directions:
            return False

        dx, dy = self.direction

        # prevent reversing against the last movement
        if len(self.segments) > 1:
            if new_direction == (-dx, -dy):
                return False

        self.next_direction = new_direction

        return True

    
    def set_boosting(self, active):
        """Start or stop boost."""

        if active and self.boost_energy <= 0:
            self.is_boosting = False
            return False

        self.is_boosting = active
        return True

    # round.py will call this method
    ## NOTE:
    """KeyController identifies the boost input.
    GameView forwards the request to Round.
    Round finds Player 1's snake and calls snake.set_boosting(True).
    Each frame, Round calls snake.update_boost(delta_time).
    Round checks snake.is_boosting to determine how frequently to call snake.move().""" 
    """GameView drives the update cycle, Round schedules gameplay movement, and Snake executes individual moves."""
    def update_boost(self, delta_time):
        """Update boost based on time."""

        if self.is_boosting:
            self.boost_energy -= self.boost_drain_rate * delta_time

            if self.boost_energy <= 0:
                self.boost_energy = 0
                self.is_boosting = False

        else:
            self.boost_energy += self.boost_regen_rate * delta_time

            self.boost_energy = min(
                self.boost_energy,
                self.max_boost_energy
            )
    