from map_objects.tile import Tile


class Map:
    """
    map of the game
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = self.initialise_tiles()

    def initialise_tiles(self):
        tiles = [[Tile(False) for y in range(self.height)] for x in range(self.width)]

        tiles[25][25].blocked = True
        tiles[25][25].block_sight = True
        tiles[26][25].blocked = True
        tiles[26][25].block_sight = True
        tiles[27][25].blocked = True
        tiles[27][25].block_sight = True

        return tiles

    def is_blocked(self, x, y):
        if self.tiles[x][y].blocked:
            return True

        return False
