"""Human input reading"""
import arcade
class KeyController:
    """Processes input from the detected keys for player snake and enemy snake"""
    def get_movement(self, key):
        """Controls Player 1 and Player 2's movements"""
        if key == arcade.key.UP:
            player = 1
            direction = (0,1)
            return (player, direction)

        if key == arcade.key.DOWN:
            player = 1
            direction = (0,-1)
            return (player, direction)

        if key == arcade.key.LEFT:
            player = 1
            direction = (-1,0)
            return (player, direction)

        if key == arcade.key.RIGHT:
            player = 1
            direction = (1,0)
            return (player, direction)

        # Controls player 2's movements
        if key == arcade.key.W:
            player = 2
            direction = (0,1)
            return (player, direction)

        if key == arcade.key.S:
            player = 2
            direction = (0,-1)
            return (player, direction)

        if key == arcade.key.A:
            player = 2
            direction = (-1,0)
            return (player, direction)

        if key == arcade.key.D:
            player = 2
            direction = (1,0)
            return (player, direction)

        return None
