spr = [
        1,
        (2, 0, 3, 9),
        (1, 1, 5, 2),
        (0, 2, 7, 2),
        (-1, 3, 9, 4)
    ]
totype = 2
def pack():
    for i in range(len(spr) - 1):
        final = ""
        rect = spr[i + 1]
        for j in range(4):
            if(j < 2):
                num = bin(rect[j] + 1)[2:]
            else:
                num = bin(rect[j])[2:]
            while len(num) < (((5 if totype == 0 else 9) if j % 2 == 0 else (6 if totype == 0 else 8)) if totype != 2 else 4):
                num = "0" + num
            final += num
        print("        " + str(int(final, 2)) + ("," if i < len(spr) - 2 else ""))
    print("REMINDER TYPE == " + str(totype))

def unpack():
    for i in range(len(spr) - 1):
        x = (spr[i + 1] >> (17 if totype == 0 else 25 if totype == 1 else 12) & (31 if totype == 0 else 511 if totype == 1 else 15)) - 1
        y = (spr[i + 1] >> (11 if totype == 0 else 17 if totype == 1 else 8) & (63 if totype == 0 else 255 if totype == 1 else 15)) - 1
        w = (spr[i + 1] >> (6 if totype == 0 else 8 if totype == 1 else 4) & (31 if totype == 0 else 511 if totype == 1 else 15))
        h = (spr[i + 1] & (63 if totype == 0 else 255 if totype == 1 else 15))
        print(f"({x},{y},{w},{h}) == {spr[i + 1]}")
pack()