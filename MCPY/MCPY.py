import ti_draw
import ti_system
import math
import time

pallete = [
    0x89b3ff,#sky
    0x05bb00,#grass
    0x804900,#dirt
    0x663931,#wood/steve hair
    0xfab737,#plank
    0x472822,#dark outline
    0x575757,#gray
    0x2c00e4,#steve pants
    0x26afff,#steve shirt
    0xe4ae7a,#skin
    0x049600#leaves
]

blocks = [
    [#grass 0
        21665,
        153122
    ],
    [#stevetop 1
        22176,
        6399209,
        8787241,
        8688776,
        6333539,
        6394947,
        6425667
    ],
    [#stevebottom 2
        22176,
        8393865,
        8492519,
        8950918
    ],
    [#dirt 3
        22178
    ],
    [#sky 4
        22176
    ],
    [#wood 5
        22179
    ],
    [#leaves 6
        22186
    ]
]

cur_x = 1
cur_y = -1
c_off_x = 1
c_off_y = -1
grounded = True

vH = 0

screen_x = 0
screen_y = -6

prev_time = time.monotonic()
time_counter = 0
time_between_frames = .2

def get_input():
    key = ti_system.wait_key()
    if(key == 92):
        return 1
    elif(key == 93):
        return 2
    elif(key == 94):
        return 3
    elif(key == 82):
        return 4
    elif(key == 83):
        return 5
    elif(key == 84):
        return 6
    elif(key == 72):
        return 7
    elif(key == 73):
        return 8
    elif(key == 74):
        return 9
    elif(key == 102):
        return 0
    elif(key == 103):
        return "."
    elif(key == 26):
        return "RIGHT"
    elif(key == 24):
        return "LEFT"
    elif(key == 25):
        return "UP"
    elif(key == 34):
        return "DOWN"
    elif(key == 105):
        return "ENTER"
    elif(key == 23):
        return "BACKSPACE"
    elif(key == 45):
        return "CLEAR"

def get_ground_level(x):
    return int(3 * math.sin(x/4))

def tree_leaves(x, y, tree_x, tree_y):
    return (x <= tree_x + 2 and x >= tree_x - 2 and y >= tree_y - 4 and y <= tree_y - 3) or (y == tree_y - 5 and x <= tree_x + 1 and x >= tree_x - 1)


def get_block(x, y):
    global cur_x
    global cur_y
    if(x == cur_x):
        if(y == cur_y - 1):
            return 1
        elif(y == cur_y):
            return 2
    ground_level = get_ground_level(x)
    if(y == ground_level):
        return 0
    elif(y > ground_level):
        return 3

    prev_closest_tree_x = x - (x % 18)
    prev_closest_tree_y = get_ground_level(prev_closest_tree_x) - 1

    next_closest_tree_x = x + (18 - (x % 18))
    next_closest_tree_y = get_ground_level(next_closest_tree_x) - 1

    if(tree_leaves(x, y, next_closest_tree_x, next_closest_tree_y) or tree_leaves(x, y, prev_closest_tree_x, prev_closest_tree_y)):
        return 6

    if(x == prev_closest_tree_x and y <= prev_closest_tree_y and y >= prev_closest_tree_y - 2):
        return 5

    return 4

def rgb(c):
    return ((c >> 16) & 255), ((c >> 8) & 255), (c & 255)

def draw_tile(tile_index, x, y, draw_c = True):
    tile = blocks[tile_index]
    for rect in tile:
        ti_draw.set_color(*rgb(pallete[rect & 31]))
        ti_draw.fill_rect(((rect >> 20) & 31) - 1 + (x * 20), ((rect >> 15) & 31) - 1 + (y * 20), (rect >> 10) & 31, (rect >> 5) & 31)
    if(x == cur_x + c_off_x - screen_x and y == cur_y + c_off_y - screen_y and draw_c):
        ti_draw.set_color(255, 255, 255)
        ti_draw.fill_rect((x * 20) - 1, (y * 20) - 1, 21, 3)
        ti_draw.fill_rect((x * 20) - 1, (y * 20) - 1, 3, 21)
        ti_draw.fill_rect((x * 20) + 17, (y * 20) - 1, 3, 21)
        ti_draw.fill_rect((x * 20) - 1, (y * 20) + 17, 21, 3)

def draw_new_screen():
    for x in range(16):
        for y in range(9):
            draw_tile(get_block(x + screen_x, y + screen_y), x, y)

def move_player(x, y):
    global cur_x
    global cur_y
    draw_tile(4, cur_x - screen_x, cur_y - screen_y)
    draw_tile(4, cur_x - screen_x, cur_y - screen_y - 1)
    draw_tile(get_block(cur_x + c_off_x, cur_y + c_off_y), cur_x - screen_x + c_off_x, cur_y - screen_y + c_off_y, False)
    cur_x += x
    cur_y += y
    draw_tile(1, cur_x - screen_x, cur_y - screen_y - 1)
    draw_tile(2, cur_x - screen_x, cur_y - screen_y)
    draw_tile(get_block(cur_x + c_off_x, cur_y + c_off_y), cur_x - screen_x + c_off_x, cur_y - screen_y + c_off_y)

def move_cursor(y, x):
    print(x)
    global c_off_x
    global c_off_y
    draw_tile(get_block(cur_x + c_off_x, cur_y + c_off_y), cur_x - screen_x + c_off_x, cur_y - screen_y + c_off_y, False)
    c_off_x += x
    c_off_y += y
    if(c_off_y > 1):
        c_off_y = 1
    elif(c_off_y < -2):
        c_off_y = -2
    if(c_off_x > 1):
        c_off_x = 1
    elif(c_off_x < -1):
        c_off_x = -1
    draw_tile(get_block(cur_x + c_off_x, cur_y + c_off_y), cur_x - screen_x + c_off_x, cur_y - screen_y + c_off_y)

draw_new_screen()
while True:
    key = ti_system.get_key(0)

    if(get_block(cur_x, cur_y + 1) != 4):
        grounded = True
        vH = 0
    else:
        if(get_block(cur_x, cur_y - 2) != 4 and vH < 0):
            vH = 0
        grounded = False

    time_counter += (time.monotonic() - prev_time)
    if(time_counter >= time_between_frames):
        if(not grounded):
            move_player(0, math.copysign(1, vH) if vH != 0 else 0)
            vH += 1
        time_counter -= time_between_frames
    prev_time = time.monotonic()

    if(key == 26 and get_block(cur_x + 1, cur_y) == 4 and get_block(cur_x + 1, cur_y - 1) == 4):
        move_player(1, 0)
    elif(key == 24 and get_block(cur_x - 1, cur_y) == 4 and get_block(cur_x - 1, cur_y - 1) == 4):
        move_player(-1, 0)
    elif(key == 25 and grounded and get_block(cur_x, cur_y - 2) == 4):
        move_player(0, -1)
        vH = -2
    elif(key == 73):
        move_cursor(-1, 0)
    elif(key == 93):
        move_cursor(1, 0)
    elif(key == 84):
        move_cursor(0, 1)
    elif(key == 82):
        move_cursor(0, -1)
    if(cur_x - screen_x >= 15):
        screen_x += 14
        draw_new_screen()
    if(cur_x - screen_x <= 0):
        screen_x -= 14
        draw_new_screen()
