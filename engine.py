import tcod as libtcod
from input_handlers import handle_keys
from entity import Entity
from render import render_all, clear_all
from map_objects.map import Map


def main():
    # initialise screen dimensions
    screen_width = 80
    screen_height = 50
    # initialise map dimensions
    map_width = 80
    map_height = 45

    # room limits and dimensions
    max_room_size = 10
    min_room_size = 6
    total_room_limit = 30

    colours = {
        'dark_wall': libtcod.Color(60, 49, 32),
        'dark_ground': libtcod.Color(96, 128, 56),
        'npc_colour': libtcod.Color(80, 80, 80)
    }

    # declare player and npcs, put them into a list
    player = Entity(int(screen_width/2), int(screen_height/2), '@', libtcod.white)
    npc = Entity(int(screen_width-10/2), int(screen_height/2), '$', colours.get('npc_colour'))
    entities = [player, npc]

    # initialise the map
    game_map = Map(map_width, map_height)
    game_map.create_map(total_room_limit, min_room_size, max_room_size, map_width, map_height, player)

    # choose font for rendering
    libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
    # initialise console
    libtcod.console_init_root(screen_width, screen_height, 'Omars Roguelike', False)

    con = libtcod.console_new(screen_width, screen_height)
    # key and mouse presses
    key = libtcod.Key()
    mouse = libtcod.Mouse()

    while not libtcod.console_is_window_closed():
        # checks for mouse or key interrupt
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)
        # renders all entities
        render_all(con, entities, screen_width, screen_height, colours, game_map)
        libtcod.console_flush()

        clear_all(con, entities)
        # checks what action has to be done
        action = handle_keys(key)

        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')

        if move:
            dx, dy = move
            if not game_map.is_blocked(player.x + dx, player.y + dy) and map_width-1 > player.x + dx > 0 and map_height-1 > \
                    player.y + dy > 0:
                player.move(dx, dy)

        if exit:
            return True

        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())


if __name__ == '__main__':
    main()