import ti_system as s
import ti_draw as d
import math

graph_size = int(input("Graph size: "))

dist = graph_size * 1.5
focal_length = dist
yaw = math.pi/4
pitch = math.pi/4

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

points = {
    "A": [-graph_size, 0, 0],
    "B": [graph_size, 0, 0],
    "C": [0, -graph_size, 0],
    "D": [0, graph_size, 0],
    "E": [0, 0, -graph_size],
    "F": [0, 0, graph_size]
}

lines = [
    ("A", "B"),
    ("C", "D"),
    ("E", "F")
]

d.set_color(0, 0, 0)

print("Format: ax + by + cz = d")

a1, b1, c1, d1 = float(input("a1: ")), float(input("b1: ")), float(input("c1: ")), float(input("d1: "))
a2, b2, c2, d2 = float(input("a2: ")), float(input("b2: ")), float(input("c2: ")), float(input("d2: "))
a3, b3, c3, d3 = float(input("a3: ")), float(input("b3: ")), float(input("c3: ")), float(input("d3: "))


def det3x3(m11, m12, m13, m21, m22, m23, m31, m32, m33):
    return m11*(m22*m33 - m23*m32) - m12*(m21*m33 - m23*m31) + m13*(m21*m32 - m22*m31)

D  = det3x3(a1, b1, c1, a2, b2, c2, a3, b3, c3)

if D == 0:
    print("\nNo unique solution.")
else:
    Dx = det3x3(d1, b1, c1, d2, b2, c2, d3, b3, c3)
    Dy = det3x3(a1, d1, c1, a2, d2, c2, a3, d3, c3)
    Dz = det3x3(a1, b1, d1, a2, b2, d2, a3, b3, d3)
    
    pox, poy, poz = Dx / D, Dy / D, Dz / D


def rotate_vector(nx, ny, nz):
    rx, ry, rz = (nx * math.cos(yaw)) - (nz * math.sin(yaw)), ny, (nx * math.sin(yaw)) + (nz * math.cos(yaw))
    rxf, ryf, rzf = rx, (ry * math.cos(pitch)) - (rz * math.sin(pitch)), (ry * math.sin(pitch)) + (rz * math.cos(pitch))
    return (rxf, ryf, rzf)

def get_projection(x, y, z):
    cam_pos = [x * math.cos(pitch) * math.sin(yaw), y * math.sin(pitch), z * math.cos(pitch) * math.cos(yaw)]
    nx, ny, nz = x - cam_pos[0], y - cam_pos[1], z - cam_pos[2]

    rx, ry, rz = rotate_vector(nx, ny, nz)
    return (focal_length * rx, focal_length * ry)

def to_screen(p):
    point = get_projection(p[0], p[1], p[2])
    x = 160 + point[0]
    y = 105 - point[1]
    return round(x, 3), round(y, 3)

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
                d.fill_rect(curX + ((ca >> 12) & 15) - 1, curY + ((ca >> 8) & 15) - 1, ((ca >> 4) & 15), (ca & 15))

        curX += 6

def draw():
    d.set_color(255, 255, 255)
    d.fill_rect(-1, -1, 321, 211)
    d.set_color(255, 0, 0)
    i = 0
    for l in lines:
        ps = [points[l[0]], points[l[1]]]
        s_ps = []
        for p in ps:
            x, y = to_screen(p)
            s_ps.append((x + 1, y + 1))
        d.draw_line(s_ps[0][0], s_ps[0][1], s_ps[1][0],
                    s_ps[1][1])
        i += 1
        d.set_color(*((0, 255, 0) if i == 1 else (0, 0, 255)))

    d.set_color(0, 0, 0)
    w_t("X", *to_screen([graph_size + 1, 0, 0]))
    w_t("Y", *to_screen([0, graph_size + 1, 0]))
    w_t("Z", *to_screen([0, 0, graph_size + 1]))

    for num in range(-graph_size, graph_size + 1, 2):
        w_t(str(round(num, 3)), *to_screen([num, 0, 0]))
        w_t(str(round(num, 3)), *to_screen([0, num, 0]))
        w_t(str(round(num, 3)), *to_screen([0, 0, num]))

    d.set_color(255, 0, 255)
    px, py = to_screen([pox, poy, poz])
    w_t(str(pox) + " " + str(poy) + " " + str(poz), px + 10, py + 10)
    d.fill_rect(px, py, 5, 5)

while True:
    draw()
    key = s.wait_key()
    if(key == 25):
        pitch -= math.pi/8
    elif(key == 34):
        pitch += math.pi/8
    elif(key == 26):
        yaw -= math.pi/8
    elif(key == 24):
        yaw += math.pi/8