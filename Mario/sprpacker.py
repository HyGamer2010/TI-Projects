spr = [
    2, 
    (4, 17,4,3),
    (11, 17,4,3)
    ]
def pack():
    for i in range(len(spr) - 1):
        final = ""
        rect = spr[i + 1]
        for j in range(4):
            if(j < 2):
                num = bin(rect[j] + 1)[2:]
            else:
                num = bin(rect[j])[2:]
            while len(num) < 5:
                num = "0" + num
            final += num
        bitcol = bin(spr[0])[2:]
        while len(bitcol) < 3:
            bitcol = "0" + bitcol
        final = bitcol + final
        print(str(int(final, 2)) + ("," if i < len(spr) - 2 else ""))

def unpack():
    for i in range(len(spr) - 1):
        c = ((spr[i + 1] >> 20) & 7)
        x = ((spr[i + 1] >> 15) & 31) - 1
        y = ((spr[i + 1] >> 10) & 31) - 1
        w = ((spr[i + 1] >> 5) & 31)
        h = (spr[i + 1] & 31)
        print(f"({c},{x},{y},{w},{h}) == {spr[i + 1]}")
pack()