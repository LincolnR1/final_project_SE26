
#here are the basic ideas of the collision detection and round setup

def __init__(self):
    #init scores to 0
    p1_score = 0
    p2_score = 0

def setup(self):
    #whatever the current map is
    #load the walls into a sprite list
    #this is happening already by default
    walls_list = all_sprite_walls
    
    #the snake_spirtes if their are multiple need to be in a list
    #sprite_list just speeds up the performance of drawing multiple sprites
    #by batch drawing
    #the snake lists cant have spatial hashing enabled, but
    #the wall list in theory can, and will be faster for it
    snake1_spirte_list = all_collidable_snake1_sprites
    snake2_sprite_list = all_collidable_snake2_sprites
    
    #clear the col_lists
    p1_col_list = []
    p2_col_list = []

    #reset round over flag
    round_over = False




def on_draw(self):
    #draws score changes, wherever we want
    arcade.draw_text(
        f"P1{p1_score}"
    )
    
    arcade.draw_text(
        f"P2{p2_score}"
    )

def update(self, delta_time):

    #every game tick, check to see collisions
    #this then adds to the snake(1/2)_col_list
    #the built in detection simply passes back 
    #a value if a sprite collides with another sprite
    #the first passed value is the collider
    #the list passed is objects its checking if it colided with

    #these are checking for collisions with walls
    p1_col_list.add(arcade.check_for_collision_with_list(snake1_head, wall_list))
    p2_col_list.add(arcade.check_for_collision_with_list(snake2_head, wall_list))

    #these check for collisions with other snake bodies
    #if snake1_head hits snake2_body, count as snake2 colliding for points

    p2_col_list.add(arcade.check_for_collision_with_list(snake1_head, snake2_spirte_list))
    p1_col_list.add(arcade.check_for_collision_with_list(snake2_head, snake1_spirte_list))

    #check for collisions
    #if any then add points reset round

    if any() in p1_col_list:
        p2_score += 1
        round_over = True

    if any in p2_col_list:
        p1_score += 1
        round_over = True

    #self.setup() starts a new round
    #will call setup(), so things that are intilized there wont carry through rounds.
    if round_over:
        self.setup()
