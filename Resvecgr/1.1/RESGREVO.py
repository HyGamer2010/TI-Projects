import ti_system
import ti_draw
import math

colors = [
    (255, 0, 0),
    (255, 126, 0),
    (255, 255, 0),
    (0, 255, 0),
    (0, 0, 255),
    (133, 0, 255)
]
letters = {
    "A": [
        82,
        40,
        850,
        16424],
    "B": [
        82,
        39,
        850,
        1618,
        16420,
        17444],
    "C": [
        98,
        39,
        1634],
    "D": [
        82,
        39,
        1618,
        16678],
    "E": [
        98,
        40,
        866,
        1634],
    "F": [
        98,
        40,
        866],
    "G": [
        98,
        39,
        9026,
        1618,
        17189],
    "H": [
        40,
        850,
        16424],
    "I": [
        98,
        8232,
        1634],
    "J": [
        98,
        8232,
        1602],
    "K": [
        40,
        850,
        16420,
        17444],
    "L": [
        39,
        1634],
    "M": [
        40,
        16424,
        4386,
        8738,
        12578],
    "N": [
        40,
        16424,
        4386,
        8738,
        13090],
    "O": [
        82,
        40,
        1618,
        16424],
    "P": [
        82,
        40,
        850,
        16421],
    "Q": [
        82,
        40,
        1602,
        16422,
        9250,
        13602,
        17954],
    "R": [
        82,
        40,
        850,
        16420,
        17444],
    "S": [
        98,
        37,
        850,
        1618,
        17189],
    "T": [
        98,
        8232],
    "U": [
        39,
        5698,
        16423],
    "V": [
        38,
        5410,
        9762,
        13602,
        16422],
    "W": [
        40,
        16424,
        5410,
        9250,
        13602],
    "X": [
        35,
        16419,
        1315,
        17699,
        4642,
        12834,
        5154,
        13346,
        8994],
    "Y": [
        34,
        16418,
        8742,
        4386,
        12578],
    "Z": [
        98,
        1634,
        1314,
        5154,
        8994,
        12834,
        16674],
    "1": [
        546,
        4386,
        8232,
        1634],
    "2": [
        82,
        1634,
        1314,
        5154,
        8994,
        12834,
        16674],
    "3": [
        82,
        850,
        1618,
        16675,
        17443],
    "4": [
        37,
        850,
        16424],
    "5": [
        98,
        37,
        850,
        1618,
        17443],
    "6": [
        98,
        39,
        866,
        1618,
        17189],
    "7": [
        98,
        16424],
    "8": [
        98,
        39,
        866,
        1618,
        16424],
    "9": [
        98,
        37,
        850,
        16424],
    "0": [
        82,
        40,
        1618,
        16424,
        4642,
        8994,
        13346],
    "+": [
        8486,
        866],
    "-": [866],
    "$": [
        354,
        292,
        850,
        1362,
        17188,
        8232],
    "/": [
        1570,
        5155,
        8994,
        12579,
        16418],
    ".": [
        9506]
}

res_color = (255, 0, 255)

def components_to_name(components):
    res_magnitude = round((components[0]**2 + components[1]**2)**(.5), 1)
    
    if(components[0] != 0 and components[1] != 0):
        reference_angle = math.atan(abs(components[1]/components[0]))
        deg_angle = round(math.degrees(reference_angle), 1)

        directions = ["EAST" if components[0] > 0 else "WEST", "NORTH" if components[1] > 0 else "SOUTH"]
        return [str(res_magnitude) + " UNITS " + str(deg_angle) + " DEGREES " + directions[1] + " OF " + directions[0], str(res_magnitude) + " UNITS " + str(round(90 - deg_angle, 1)) + " DEGREES " + directions[0] + " OF " + directions[1]]
    else:
        direction = "NORTH" if components[1] > 0 else "EAST" if components[0] > 0 else "SOUTH" if components[1] < 0 else "WEST"
        return [str(res_magnitude) + " UNITS " + direction]

def calc_vec(angle, magnitude):
    return [magnitude * math.cos(angle), magnitude * math.sin(angle)]

def draw_vec(startpt, components, scalar):
    startpt = [int(startpt[0] * scalar + 159), int(-startpt[1] * scalar + 95)]
    endpt = [int(startpt[0] + components[0] * scalar), int(startpt[1] - components[1] * scalar)]

    ti_draw.draw_line(startpt[0], startpt[1], endpt[0], endpt[1])

    vec_angle = math.atan2(components[1], components[0])

    arrow_parts = [calc_vec(vec_angle + math.pi/4, 7.5), calc_vec(vec_angle - math.pi/4, 7.5)]
    for part in arrow_parts:
        ti_draw.draw_line(endpt[0], endpt[1], endpt[0] - part[0], endpt[1] + part[1])

def w_t(text : str, x, y):
    curX = x
    curY = y
    for char in text:
        if(char == "|"):
            curY += 8
            curX = x
            continue

        if(char in letters):
            for ca in letters[char]:
                try:
                    ti_draw.fill_rect(curX + ((ca >> 12) & 15) - 1, curY + ((ca >> 8) & 15) - 1, ((ca >> 4) & 15), (ca & 15))
                except Exception as e:
                    print(e)
                    print(curX + ((ca >> 12) & 15) - 1, curY + ((ca >> 8) & 15) - 1, ((ca >> 4) & 15), (ca & 15))
                    print(char)
        curX += 6

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

def text_box(text:str, starting_line, col):
    lines = text.count("|") + 1

    ti_draw.set_color(255, 255, 255)
    ti_draw.fill_rect(2, 180 + starting_line * 8, 315, lines * 8 + 1)

    ti_draw.set_color(*col)
    w_t(text, 3, 181 + starting_line * 8)

def get_numeric_input_str(writing_line, col):
    ans_str = ""
    while True:
        pressed = get_input()
        if(type(pressed) is int or pressed == "."):
            ans_str += str(pressed)
        elif(pressed == "BACKSPACE"):
            ans_str = ans_str[:len(ans_str) - 1]
        elif(pressed == "ENTER"):
            return ans_str
        text_box(ans_str, writing_line, col)

def yes_no_sel(starting_line, col):
    text_box("Y  N", starting_line, col)
    sel_on_first = True
    while True:
        if(sel_on_first):
            ti_draw.set_color(*col)
        else:
            ti_draw.set_color(255, 255, 255)
        ti_draw.fill_rect(2, 188 + starting_line * 8, 6, 2)

        if(not sel_on_first):
            ti_draw.set_color(*col)
        else:
            ti_draw.set_color(255, 255, 255)
        ti_draw.fill_rect(20, 188 + starting_line * 8, 6, 2)

        pressed = get_input()
        if(pressed == "RIGHT" or pressed == "LEFT"):
            sel_on_first = not sel_on_first
        elif(pressed == "ENTER"):
            return sel_on_first

def clear_text_box():
    ti_draw.set_color(255, 255, 255)
    ti_draw.fill_rect(2, 180, 315, 50)

def clear_cartesian():
    ti_draw.set_color(255, 255, 255)
    ti_draw.fill_rect(77, 13, 165, 165)
    ti_draw.set_color(0, 0, 0)
    ti_draw.fill_rect(158, 15, 3, 161)
    ti_draw.fill_rect(79, 94, 161, 3)

while True:
    cur_vec = 0

    vecs = []
    components = [0, 0]
    largest_components = [0, 0]

    while True:
        col = colors[cur_vec]

        clear_cartesian()

        text_box("WHAT IS THE LENGTH OF THE VECTOR?", 0, col)
        mag = float(get_numeric_input_str(1, col))

        clear_text_box()
        text_box("DOES THE ANGLE LIE ON AN AXIS?", 0, col)
        on_axis = yes_no_sel(1, col)

        if(not on_axis):
            clear_text_box()
            text_box("WHAT IS THE ANGLE OF THE VECTOR?", 0, col)
            angle = float(get_numeric_input_str(1, col))

        clear_text_box()
        text_box("CHOOSE THE INITIAL AXIS", 0, col)
        axis = 1
        while True:
            clear_cartesian()

            ti_draw.set_color(*col)
            if(axis == 1):
                ti_draw.fill_rect(158, 15, 3, 79)
            if(axis == 2):
                ti_draw.fill_rect(161, 94, 79, 3)
            if(axis == 3):
                ti_draw.fill_rect(158, 97, 3, 79)
            if(axis == 4):
                ti_draw.fill_rect(79, 94, 79, 3)

            pressed = get_input()
            if(pressed == "UP" or pressed == "RIGHT"):
                axis += 1
                if(axis > 4):
                    axis = 1
            elif(pressed == "DOWN" or pressed == "LEFT"):
                axis -= 1
                if(axis < 1):
                    axis = 4
            elif(pressed == "ENTER"):
                break

        if(on_axis):
            if(axis == 1):
                vec = [0, mag]
            elif(axis == 2):
                vec = [mag, 0]
            elif(axis == 3):
                vec = [0, -mag]
            elif(axis == 4):
                vec = [-mag, 0]
        else:
            if(axis == 1 or axis == 3):
                angle = 90.0 - angle

            text_box("CHOOSE A QUADRANT", 0, col)
            quadrant = 1
            while True:
                clear_cartesian()

                ti_draw.set_color(*col)
                if(quadrant == 1):
                    ti_draw.fill_rect(160, 15, 80, 80)
                elif(quadrant == 2):
                    ti_draw.fill_rect(79, 15, 80, 80)
                elif(quadrant == 3):
                    ti_draw.fill_rect(79, 96, 80, 80)
                elif(quadrant == 4):
                    ti_draw.fill_rect(160, 96, 80, 80)

                pressed = get_input()
                if(pressed == "UP" or pressed == "RIGHT"):
                    quadrant += 1
                    if(quadrant > 4):
                        quadrant = 1
                elif(pressed == "DOWN" or pressed == "LEFT"):
                    quadrant -= 1
                    if(quadrant < 1):
                        quadrant = 4
                elif(pressed == "ENTER"):
                    if(quadrant == 2):
                        angle = 180 - angle
                    elif(quadrant == 3):
                        angle += 180
                    elif(quadrant == 4):
                        angle = 360 - angle
                    break
            vec = [mag * math.cos(math.radians(angle)), mag * math.sin(math.radians(angle))]

        clear_cartesian()
        clear_text_box()

        ti_draw.set_color(*col)
        draw_vec([0, 0], vec, 80 / (abs(vec[0]) if abs(vec[0]) > abs(vec[1]) else abs(vec[1])))

        text_box("DOES THIS LOOK CORRECT?", 0, col)
        if(yes_no_sel(1, col)):
            vecs.append(vec)
            components[0] += vec[0]
            components[1] += vec[1]

            if(abs(components[0]) > largest_components[0]):
                largest_components[0] = abs(components[0])
            if(abs(components[1]) > largest_components[1]):
                largest_components[1] = abs(components[1])
            cur_vec += 1

        clear_text_box()
        if(len(vecs) > 1):
            text_box("IS THIS THE FINAL VECTOR?", 0, col)
            if(yes_no_sel(1, col)):
                break
        clear_text_box()
        
    clear_cartesian()
    scalar_opts = [80 / largest_components[0], 80 / largest_components[1]]

    scalar = scalar_opts[0] if scalar_opts[0] < scalar_opts[1] else scalar_opts[1]

    ti_draw.set_color(0, 0, 0)
    ti_draw.fill_rect(158, 15, 3, 161)
    ti_draw.fill_rect(79, 94, 161, 3)

    ti_draw.set_pen("medium", "solid")
    prev_vec = [0, 0]
    cur_c_ind = 0
    for vec in vecs:
        ti_draw.set_color(*(colors[cur_c_ind]))
        draw_vec(prev_vec, vec, scalar)
        prev_vec = [prev_vec[0] + vec[0], prev_vec[1] + vec[1]]
        cur_c_ind += 1

    ti_draw.set_color(*res_color)
    draw_vec([0, 0], components, scalar)

    ti_draw.set_pen("thin", "solid")

    vecs.append(components)

    looking_at_vecs = True
    selected_vec = len(vecs) - 1

    while(looking_at_vecs):
        text = components_to_name(vecs[selected_vec])

        ti_draw.set_color(255, 255, 255)
        ti_draw.fill_rect(2, 180, 315, 25)

        if(selected_vec < len(vecs) - 1):
            col = colors[selected_vec]
        else:
            col = res_color
        ti_draw.set_color(*col)

        if(len(text) == 1):
            w_t(text[0], 3, 181)
        else:
            w_t(text[0] + "|OR|" + text[1], 3, 181)

        key = ti_system.wait_key()
        if(key == 105):
            looking_at_vecs = False
        elif(key == 24):
            selected_vec -= 1
            if(selected_vec < 0):
                selected_vec = len(vecs) - 1
        elif(key == 26):
            selected_vec += 1
            if(selected_vec > len(vecs) - 1):
                selected_vec = 0
    clear_text_box()