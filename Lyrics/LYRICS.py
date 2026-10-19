import ti_draw
import ti_system
import time

songs = {
    "STORY OF A WARRIOR": [
        [4.53,"I HEARD OF A MAN, A LEGEND OF OLD"],
        [8.79,"WHO SEARCHED FOR A HEART HE COULD HOLD"],
        [13.57,"ALL THROUGH THE LAND, HIS STORY WAS TOLD"],
        [18.04,"PASSED DOWN THROUGH ALL THE LONELY SOULS"],
        [23.85,"SO IF YOU WANT TO HEAR, LEND YOUR EAR AND"],
        [29.28,"I'LL TELL YOU THE STORY OF A WARRIOR"],
        [35.78,"WHO FOUGHT THE FIGHT OF LOVE (OOH)"],
        [39.74,"WITH EVERY WOUND HE WORE"],
        [42.41,"HE RAISED HIS SWORD AND"],
        [44.96,"MARCHED THROUGH TEARS AND BLOOD (OOH)"],
        [49.05,"AND THOUGH HIS FOES LEFT HIM BROKEN"],
        [51.28,"HE AROSE WITH A HOPE INSIDE HIS HEART"],
        [55.38,"RIGHT THROUGH THE SCARS"],
        [57.35,"NOW THEY TELL THE STORY OF A WARRIOR"],
        [62.69,"WHO FOUGHT THE FIGHT"],
        [64.95,"WHO FOUGHT THE FIGHT OF LOVE"],
        [69.5,"THROUGH FIRE AND RAIN, HIS HEART SET ABLAZE"],
        [74.05,"NO MATTER THE PAIN, HE SET HIS SOUL ON FIRE"],
        [79.73,"HELD HIS HEAD UP HIGHER"],
        [82.01,"WHEN YOU HEAR HIS NAME, THEY'LL SAY"],
        [85.39,"I'LL TELL YOU THE STORY OF A WARRIOR"],
        [91.86,"WHO FOUGHT THE FIGHT OF LOVE (OOH)"],
        [95.82,"WITH EVERY WOUND HE WORE"],
        [98.57,"HE RAISED HIS SWORD AND"],
        [101.01,"MARCHED THROUGH TEARS AND BLOOD (OOH)"],
        [105.35,"AND THOUGH HIS FOES LEFT HIM BROKEN"],
        [107.24,"HE AROSE WITH A HOPE INSIDE HIS HEART"],
        [111.43,"RIGHT THROUGH THE SCARS"],
        [113.43,"NOW THEY TELL THE STORY OF A WARRIOR"],
        [118.75,"WHO FOUGHT THE FIGHT"],
        [121.04,"WHO FOUGHT THE FIGHT OF LOVE"]
    ]
}

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
                ti_draw.fill_rect(curX + ((ca >> 12) & 15) - 1, curY + ((ca >> 8) & 15) - 1, ((ca >> 4) & 15), (ca & 15))
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

ti_draw.set_color(0, 0, 0)

w_t("CHOOSE A SONG:", 2, 2)

num = 1
for song in songs:
    w_t(song, 2, 10 + num * 8)
    num += 1

num = 0
while True:
    ti_draw.set_color(255, 255, 255)
    ti_draw.fill_rect(311, 0, 7, 241)
    ti_draw.set_color(0, 0, 0)
    ti_draw.fill_rect(311, 18 + num * 8, 7, 7)

    pressed = get_input()
    if(pressed == "UP"):
        num -= 1
        if(num < 0):
            num = 0
    elif(pressed == "DOWN"):
        num += 1
        if(num >= len(songs)):
            num = len(songs) - 1
    elif(pressed == "ENTER"):
        sel_song = songs[list(songs.keys())[num]]
        break

ti_draw.set_color(255, 255, 255)
ti_draw.fill_rect(-1, -1, 321, 241)

ti_draw.set_color(0, 0, 0)
w_t("3", 2, 2)
time.sleep(1)
w_t("2", 2, 10)
time.sleep(1)
w_t("1", 2, 18)
time.sleep(1)
ti_draw.set_color(255, 255, 255)
ti_draw.fill_rect(-1, -1, 321, 241)
ti_draw.set_color(0, 0, 0)
w_t("START", 2, 2)

start_time = time.monotonic()
for lyric in sel_song:
    needed_time = start_time + lyric[0] - .1
    while True:
        if(time.monotonic() >= needed_time):
            ti_draw.set_color(255, 255, 255)
            ti_draw.fill_rect(-1, -1, 321, 241)
            ti_draw.set_color(0, 0, 0)
            w_t(lyric[1], 2, 2)
            break


