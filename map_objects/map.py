from map_objects.tile import Tile
from map_objects.rectangle import Rectangle

class Map:
    """
    map of the game
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = self.initialise_tiles()

    def initialise_tiles(self):
        tiles = [[Tile(True) for y in range(self.height)] for x in range(self.width)]

        return tiles

    def create_map(self):
        room1 = Rectangle(20, 15, 15, 10)
        room2 = Rectangle(35, 15, 15, 10)

        self.create_room(room1)
        self.create_room(room2)

    def create_room(self, room):
        for x in range(room.xStart + 1, room.xEnd):
            for y in range(room.yStart + 1, room.yEnd):
                self.tiles[x][y].blocked = False
                self.tiles[x][y].block_sight = False

    def is_blocked(self, x, y):
        if self.tiles[x][y].blocked:
            return True

        return False
