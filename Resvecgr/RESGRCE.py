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

def draw_vec(startpt, components, scalar):
    startpt = [int(startpt[0] * scalar + 118), int(-startpt[1] * scalar + 71)]
    endpt = [int(startpt[0] + components[0] * scalar), int(startpt[1] - components[1] * scalar)]

    ti_draw.draw_line(startpt[0], startpt[1], endpt[0], endpt[1])

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

while(True):
    vecs = []
    first_vec = True
    last_vec = False
    components = [0, 0]
    largest_components = [0, 0]
    while(not last_vec):
        magnitude = float(input("What is the length of the vector?\n"))
        on_axis = input("Does your angle lie on an axis?\n1: Yes\n2: No\n") == "1"
        if(on_axis):
            direction = input("What axis does it lie on?\n1. North\n2. East\n3. South\n4. West\n")
            if(direction == "1"):
                components[1] += magnitude
                vecs.append([0, magnitude])
            elif(direction == "2"):
                components[0] += magnitude
                vecs.append([magnitude, 0])
            elif(direction == "3"):
                components[1] -= magnitude
                vecs.append([0, -magnitude])
            elif(direction == "4"):
                components[0] -= magnitude
                vecs.append([-magnitude, 0])
        else:
            angle = input("Fill in the blank: ____ degrees _____ of _____\nWhat is the angle?\n")
            direction = int(input("Fill in the blank: " + angle + " degrees _____ of _____\nWhat is the direction?\n1. North\n2. East\n3. South\n4. West\n"))
            if(direction == 1):
                dirname = "North"
            elif(direction == 2):
                dirname = "East"
            elif(direction == 3):
                dirname = "South"
            elif(direction == 4):
                dirname = "West"
            
            axis = int(input("Fill in the blank: " + angle + " degrees " + dirname + " of _____\nWhat is the base axis?\n1. North\n2. East\n3. South\n4. West\n"))
            angle = float(angle)

            if(axis == 1 or axis == 3):
                angle = 90.0 - angle

            angle = math.radians(angle)

            xcomp = magnitude * math.cos(angle)
            ycomp = magnitude * math.sin(angle)

            if(axis == 4 or direction == 4):
                xcomp = -xcomp
            if(axis == 3 or direction == 3):
                ycomp = -ycomp
            components[0] += xcomp
            components[1] += ycomp
            vecs.append([xcomp, ycomp])

        if(abs(components[0]) > largest_components[0]):
            largest_components[0] = abs(components[0])
        if(abs(components[1]) > largest_components[1]):
            largest_components[1] = abs(components[1])
        
        if(first_vec):
            first_vec = False
        else:
            last_vec = input("Is that the last vector?\n1. Yes\n2. No\n") == "1"

    scalar_opts = [70 / largest_components[0], 70 / largest_components[1]]

    scalar = scalar_opts[0] if scalar_opts[0] < scalar_opts[1] else scalar_opts[1]

    ti_draw.set_color(0, 0, 0)
    ti_draw.fill_rect(118, 2, 3, 141)
    ti_draw.fill_rect(49, 71, 141, 3)

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
            w_t(text[0], 1, 149)
        else:
            w_t(text[0] + "|OR|" + text[1], 1, 149)

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
    print("\n\n\n\n")