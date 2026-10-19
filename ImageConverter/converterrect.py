from PIL import Image

img = Image.open("3.jpg").copy()

w_scalar = 64 / img.width
h_scalar = 48 / img.height

if(w_scalar < h_scalar):
    new_w = img.height * 1.5
    crop = (img.width - new_w) / 2
    img = img.crop([crop, 0, img.width - crop, img.height])

elif(h_scalar < w_scalar):
    new_h = img.width / 1.5
    crop = (img.height - new_h) / 2
    img = img.crop([0, crop, img.width, img.height - crop])

img = img.resize([64, 48], Image.Resampling.BILINEAR)

out = ""

colors = []

for w in range(64):
    for h in range(48):
        pix = list(img.getpixel([w, h]))
        for i in range(3):
            pix[i] = (pix[i] // 16) * 16

        col = (pix[0], pix[1], pix[2])
        img.putpixel((w, h), col)

        if(col not in colors):
            colors.append(col)

rects = []

for color in colors:
    bounds = [64, 48, 0, 0]
    for x in range(64):
        for y in range(48):
            if(img.getpixel([x, y]) == color):
                if(x < bounds[0]):
                    bounds[0] = x
                if(x > bounds[2]):
                    bounds[2] = x
                if(y < bounds[1]):
                    bounds[1] = y
                if(y > bounds[3]):
                    bounds[3] = y
    rects.append([color, bounds, (bounds[2] - bounds[0] + 1) * (bounds[3] - bounds[1] + 1)])

empty_image = Image.new("1", (64, 48), 1)
covered_img = empty_image.copy()

final_rects = []

current_allowed = empty_image.copy()
already_drawn = empty_image.copy()
for rect in rects:
    current_allowed.paste(empty_image)
    already_drawn.paste(empty_image)
    for x in range(64):
        for y in range(48):
            color = rect[0]
            bounds = rect[1]
            if((x >= bounds[0] and x <= bounds[2] and y >= bounds[1] and y <= bounds[3]) and (img.getpixel((x, y)) == color or covered_img.getpixel((x, y)) == 1)):
                current_allowed.putpixel((x, y), 0)

    #current_allowed.show()
    #input()

    for x in range(64):
        for y in range(48):
            if(current_allowed.getpixel((x, y)) == 0 and already_drawn.getpixel((x, y)) == 1):
                size = 0

                i = 0
                while y + i <= 47:
                    if(current_allowed.getpixel((x, y + i)) == 1):
                        break
                    if(already_drawn.getpixel((x, y + i)) == 1):
                        size = i + 1
                    i += 1

                prev_uncovered = 0
                rect = [x, y, 0, 0]
                for h in range(size):
                    i = 0
                    sizeX = 0
                    uncovered = 0
                    while x + i <= 63:
                        if(current_allowed.getpixel((x + i, y + h)) == 1):
                            break
                        if(already_drawn.getpixel((x + i, y + h)) == 1):
                            sizeX = i + 1
                        i += 1

                    min_size = 64
                    for nH in range(h):
                        cur_size = 0
                        for nW in range(sizeX):
                            if(current_allowed.getpixel((x + nW, y + nH)) == 0):
                                cur_size += 1
                            else:
                                break
                        if(cur_size < min_size):
                            min_size = cur_size

                            

                    for nH in range(h):
                        for nW in range(min_size):
                            if(already_drawn.getpixel((x + nW, y + nH)) == 1):
                                uncovered += 1

                    if(uncovered > prev_uncovered):
                        rect[2] = x + min_size
                        rect[3] = y + size
                    i += 1

                final_rects.append([color, rect])

                for nX in range(64):
                    for nY in range(48):
                        if(nX >= rect[0] and nX <= rect[2] and nY >= rect[1] and nY <= rect[3]):
                            covered_img.putpixel((nX, nY), 0)
                            already_drawn.putpixel((nX, nY), 0)


                    

                


final_rects.reverse()

for rect in final_rects:
    color = rect[0]
    bounds = rect[1]
    for nX in range(64):
        for nY in range(48):
            if(nX >= bounds[0] and nX <= bounds[2] and nY >= bounds[1] and nY <= bounds[3]):
                img.putpixel((nX, nY), color)

print(final_rects)

            

img.show()