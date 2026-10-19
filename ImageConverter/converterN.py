from PIL import Image
import sys
import string

def base16_to_36(n):
    num = int(n, 16)
    if(num == 0):
        return "0"

    digs = string.digits + string.ascii_lowercase

    result = ""
    while num > 0:
        rem = num % 36
        num //= 36
        result += digs[rem:rem + 1]

    return result

img = Image.open("5.jpg")

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

for w in range(64):
    for h in range(48):
        pix = img.getpixel([w, h])
        for i in range(3):
            hex_num = hex(pix[i])[2:8]
            if(len(hex_num) < 2):
                hex_num = "0" + hex_num
            out += hex_num[:1]

with open("out.txt", "w") as file:
    file.write(out)
img.show()