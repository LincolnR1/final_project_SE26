"""Controls snake position and state (collision, length, boost, etc)"""

class Snake:
    """Represents a snake on the grid"""

    def __init__(self, start_position, direction=(1,0), length=3):
        self.direction = direction
        self.segments = []

        

        for i in range(length):
            x = start_position[0] - i * direction[0]
            y = start_position[1] - i * direction[1]

            self.segments.append((x,y))

        self.pending_growth = 0

