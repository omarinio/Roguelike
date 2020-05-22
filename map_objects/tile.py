class Tile:
    """
    Map tiles, can be blocked and can block sight
    """
    def __init__(self, blocked, block_sight=None):
        self.blocked = blocked

        # if tile is blocked, it blocks sight by default
        if block_sight is None:
            block_sight = blocked

        self.block_sight = block_sight
