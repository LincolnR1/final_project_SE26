
#here are the basic ideas of the collision detection and round setup
import arcade

# NOTE: eventually this file will be moving the snakes instead of game_view
# the stuff I have added is built with that in mind but could also be altered

    

CELL_SIZE = 32

class Round:
    """Manages gameplay for the current round."""

    def __init__(self, snake1, snake2, wall_sprites):
        self.snakes = {
            1: snake1,
            2: snake2
        }

        self.snake_visuals = {
            1: SnakeSprites(snake1),
            2: SnakeSprites(snake2)
        }
   
        
        #both accessible as self.snakes[1 or 2] and self.snake_visuals[1 or 2]

        self.wall_sprites = wall_sprites

        self.move_timers = {
            1: 0.0,
            2: 0.0
        } 

        self.normal_interval = 0.15
        self.boost_interval = 0.075

        # keep track of lives
        self.lives = {
            1: 3,
            2: 3
        }

        # keep track of time till respawn
        self.respawn_timers = {
            1: 0.0,
            2: 0.0
        }

        # whether a snake is respawning currently
        self.respawning = {
            1: False,
            2: False
        }

        self.respawn_delay = 1.5

    def update(self, delta_time):

        for player, snake in self.snakes.items():
            snake.update_boost(delta_time)

            if snake.is_boosting:
                interval = self.boost_interval
            else:
                interval = self.normal_interval

            self.move_timers[player] += delta_time

            while self.move_timers[player] >= interval:
                snake.move()
                self.snake_visuals[player].sync_positions()

                # check for wall collisions
                if self.check_wall_collision(self.snake_visuals[player].sprites):
                    print(f"Player {player} hit a wall")

                # check for snake collisions
                if self.check_snake_collision(self.snake_visuals[player].sprites):
                    print(f"Player {player} hit the opponent")

                self.move_timers[player] -= interval

    def check_wall_collision(self, player):
        """Check if there are collisions between a players head and walls"""
        head = player[0]

        collisions = arcade.check_for_collision_with_list(
            head,
            self.wall_sprites
        )

        return bool(collisions)

    def check_snake_collision(self, player):
        """Check is there are collisions between players"""
        head = player[0]

        opponent = 2 if player == 1 else 1

        opponent_sprites = self.snake_visuals[opponent].sprites

        collisions = arcade.check_for_collision_with_list(
            head,
            opponent_sprites
        )

        return bool(collisions)

    def handle_collision(self, player):
        if self.respawning[player]:
            return

        self.lives[player] -= 1

        print(f"Player {player} lost a life!")
        print(f"Lives remaining: {self.lives[player]}")

        if self.lives[player] <= 0:
            print(f"Player {player} is eliminated!")
            self.respawning[player] = True
            return

        self.respawning[player] = True
        self.respawn_timers[player] = self.respawn_delay

def grid_to_pixel(pos):
    """Helper function to convert a grid position to pixel coordinates"""
    x, y = pos

    return (x * CELL_SIZE + CELL_SIZE / 2, y * CELL_SIZE + CELL_SIZE / 2)

class SnakeSprites:
    """Class to manage the snakes as SpriteLists while keeping movement
    logic seperate in snake.py, observes the snakes state and updates sprites accordingly"""

    #NOTE:eventually when Round moves a snake it will look like:
    #
    # init()
    #   self.snake_visual = SnakeSprites(self.snake)
    #
    # on_update()
    #   snake.move() - moves the acutal snake
    #   snake_visual.sync_positions() - observes the snake and updates sprites 
    #
    # on_draw() in game_view
    #   self.snake_visual.sprites.draw()
    # 
    # all of that together will move the snake and update the
    # sprites(which are more like hitboxes) to match so collisions 
    # can be checked using arcades functions

    def __init__(self, snake):
        self.snake = snake
        self.sprites = arcade.SpriteList()

        for position in self.snake.segments:
            sprite = arcade.SpriteSolidColor(
                CELL_SIZE, 
                CELL_SIZE, 
                color=snake.color
            )

            sprite.position = grid_to_pixel(position)

            self.sprites.append(sprite)
        # allows us to identify the head as head_sprite = self.sprites[0]

    def sync_positions(self):
        """Update sprite positions to match snake segments"""
        for sprite, position in zip(
            self.sprites, 
            self.snake.segments
        ):
            sprite.position = grid_to_pixel(position)
    
    @property
    def head(self):
        """Return  snakes head sprite, allows access as '{variable_for_snake_sprite}.head'"""
        return self.sprites[0]
    