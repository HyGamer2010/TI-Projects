spr = [
        (-1, -1, 21, 21, 10)
    ]
def pack():
    for i in range(len(spr)):
        final = ""
        rect = spr[i]
        for j in range(5):
            if(j < 2):
                num = bin(rect[j] + 1)[2:]
            else:
                num = bin(rect[j])[2:]
            while len(num) < 5:
                num = "0" + num
            final += num
        print("        " + str(int(final, 2)) + ("," if i < len(spr) - 1 else ""))

# def unpack():
#     for i in range(len(spr) - 1):
#         x = (spr[i + 1] >> (17 if totype == 0 else 25 if totype == 1 else 12) & (31 if totype == 0 else 511 if totype == 1 else 15)) - 1
#         y = (spr[i + 1] >> (11 if totype == 0 else 17 if totype == 1 else 8) & (63 if totype == 0 else 255 if totype == 1 else 15)) - 1
#         w = (spr[i + 1] >> (6 if totype == 0 else 8 if totype == 1 else 4) & (31 if totype == 0 else 511 if totype == 1 else 15))
#         h = (spr[i + 1] & (63 if totype == 0 else 255 if totype == 1 else 15))
#         print(f"({x},{y},{w},{h}) == {spr[i + 1]}")
pack()