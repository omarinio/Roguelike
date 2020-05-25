from map_objects.tile import Tile
from map_objects.rectangle import Rectangle
from random import randint


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

    def create_map(self, total_room_limit, min_room_size, max_room_size, width, height, player):
        rooms = []
        num_rooms = 0

        for r in range(total_room_limit):
            w = randint(min_room_size, max_room_size)
            h = randint(min_room_size, max_room_size)

            x = randint(0, width - w - 1)
            y = randint(0, height - h - 1)

            new_room = Rectangle(x, y, w, h)

            for room in rooms:
                if new_room.intersect(room):
                    break
            else:
                self.create_room(new_room)

                (new_x, new_y) = new_room.center()

                if num_rooms == 0:
                    player.x = new_x
                    player.y = new_y
                else:
                    (prev_x, prev_y) = rooms[num_rooms - 1].center()

                    if randint(0, 1) == 1:
                        self.vertical_tunnel(prev_y, new_y, prev_x)
                        self.horizontal_tunnel(prev_x, new_x, prev_y)
                    else:
                        self.horizontal_tunnel(prev_x, new_x, prev_y)
                        self.vertical_tunnel(prev_y, new_y, prev_x)

                rooms.append(new_room)
                num_rooms += 1

    def create_room(self, room):
        for x in range(room.x_start + 1, room.x_end):
            for y in range(room.y_start + 1, room.y_end):
                self.tiles[x][y].blocked = False
                self.tiles[x][y].block_sight = False

    def horizontal_tunnel(self, x1, x2, y):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            self.tiles[x][y].blocked = False
            self.tiles[x][y].block_sight = False

    def vertical_tunnel(self, y1, y2, x):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            self.tiles[x][y].blocked = False
            self.tiles[x][y].block_sight = False

    def is_blocked(self, x, y):
        if self.tiles[x][y].blocked:
            return True

        return False
