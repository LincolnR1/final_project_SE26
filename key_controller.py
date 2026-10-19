"""Human input reading"""
import arcade
class KeyController:
    # processes input from the detected keys

    def get_movement(self, key):
        # controls player 1's movements
        if key == arcade.key.UP:
            player = 1
            direction = (0,1)
            return (player, direction)

        elif key == arcade.key.DOWN:
            player = 1
            direction = (0,-1)
            return (player, direction)

        elif key == arcade.key.LEFT:
            player = 1
            direction = (-1,0)
            return (player, direction)

        elif key == arcade.key.RIGHT:
            player = 1
            direction = (1,0)
            return (player, direction)

    # Controls player 2's movements
        elif key == arcade.key.W:
            player = 2
            direction = (0,1)
            return (player, direction)

        elif key == arcade.key.S:
            player = 2
            direction = (0,-1)
            return (player, direction)

        elif key == arcade.key.A:
            player = 2
            direction = (-1,0)
            return (player, direction)

        elif key == arcade.key.D:
            player = 2
            direction = (1,0)
            return (player, direction)

        else:
            return None


