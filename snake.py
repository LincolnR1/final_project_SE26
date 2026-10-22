"""Controls snake position and state (collision, length, boost, etc)"""

class Snake:
    """Represents a snake on the grid"""

    def __init__(self, start_position, direction=(1,0), length=3):
        self.direction = direction
        self.next_direction = direction
        self.segments = []

        

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
        