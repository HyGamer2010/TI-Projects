import numpy
from PIL import Image
img = Image.open("Ref/map1-1.png")
pts = numpy.array(img)

rows = []

img_w = 224
img_h = 12

for y in range(img_h):
    cur_row = ""
    for x in range(img_w):
        col = pts[y, x]
        cur_row += ("001" if numpy.array_equal(col, [200, 76, 12, 255]) else "010" if numpy.array_equal(col, [150, 56, 9, 255]) else "011" if numpy.array_equal(col, [252, 188, 176, 255]) else "100" if numpy.array_equal(col, [252, 152, 56, 255]) else "101" if numpy.array_equal(col, [0, 168, 0, 255]) else "110" if numpy.array_equal(col, [128, 208, 16, 255]) else "000")
    rows.append(int(cur_row, 2))
print(rows)

