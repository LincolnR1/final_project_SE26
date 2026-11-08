"""Maps class"""
import arcade
import consts

class Maps(arcade.Window):
    """Load in the maps here."""
    def __init__(self):
        """Call the parent class to set up the window"""
        super().__init__(consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT,
                         consts.WINDOW_TITLE, center_window=True)
        # self.tile_map
        self.physics_engine = None
        self.tile_map = None
        self.scene = None

    def setup(self):
        """Loads in all the snake games maps here"""
        layer_options = {
            "Walls": {"use_spatial_hash": True,
                      "scaling": 1.0},
            "Background": {"use_spatial_hash": False,
                           "scaling": 1.0},
            }
        self.tile_map = arcade.load_tilemap("maps/CS3050_final_project_level1.tmx",
                                            scaling=1, layer_options=layer_options)
        self.scene = arcade.Scene.from_tilemap(self.tile_map)
#       self.physics_engine = arcade.PhysicsEngineSimple(walls=self.scene["Walls"])

    def update(self):
        """Updates the games collisions"""
        self.physics_engine.update()

    def on_draw(self):
        """Render the screen."""
        self.clear()
        self.scene.draw()
