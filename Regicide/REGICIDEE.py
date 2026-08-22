import ti_draw as d
import ti_system as s
from ti_draw import fill_rect as f

c_b = None
j, q, k = 12, 13, 14
spade, club, heart, diamond = 3, 2, 0, 1

left_in_rank = 4
c_rank = j

hovers = {
    "Suits": [
        [(28, 113),(92, 113),(156,113),(220,113),(286,113)]
    ],
    "Sel1": [
        [(27, 144),(91, 144),(158,144),(219,144),(285,144)],
        [(27, 166),(91, 166),(158,166),(219,166),(285,166)],
        [(27, 188),(91, 188),(158,188),(219,188),(285,188)]
    ],
    "Sel2": [
        [(27, 144),(91, 144),(158,144),(219,144)],
        [(27, 166),(91, 166),(158,166),(219,166)],
        [(27, 188),(221, 190)]
    ]
}

letters_sm = {
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
letters_bg = {
    "1": [
        12346,
        8483,
        4642,
        6514
    ],
    "2": [
        4403,
        8274,
        20788,
        17458,
        13618,
        9778,
        5940,
        14674
    ],
    "3": [
        4402,
        8274,
        20788,
        13378,
        21813,
        6194,
        10578
    ],
    "4": [
        4150,
        20539,
        13362
    ],
    "5": [
        4210,
        4404,
        5218,
        21813,
        6194,
        10578
    ],
    "6": [
        8274,
        20786,
        4409,
        13378,
        21813,
        10578
    ],
    "7": [
        4210,
        20787,
        17202,
        13367
    ],
    "8": [
        8274,
        9298,
        10578,
        4404,
        20788,
        5429,
        21813
    ],
    "9": [
        8274,
        9298,
        4404,
        20793,
        6194,
        10578
    ],
    "0": [
        8274,
        4409,
        20793,
        10578
    ],
    "J": [
        146,
        12602,
        2083,
        6450
    ],
    "Q": [
        4210,
        313,
        6482,
        24888,
        13874,
        18226,
        22578,
        26930
    ],
    "K": [
        59,
        9027,
        16946,
        20786,
        24626,
        17714,
        22066,
        26420
    ],
    "A": [
        4194,
        314,
        20794,
        9282
    ],
    "h": [
        661,
        4407,
        20791,
        9811,
        14386
    ],
    "d": [
        12601,
        8791,
        4981,
        1171
    ],
    "c": [
        12601,
        1427,
        8787,
        5157,
        25637
    ],
    "s":[
        12601,
        8786,
        4978,
        1172
    ]
}
c_ho = [0, 0]
c_grp = "Suits"

c_he = 0
c_at = 0

sel_suit = None
cur_cards = []
negated = False

sel_cards = []

def w_t(text : str, x, y, sm):
    curX = x
    curY = y
    for char in text:
        if(char == "|"):
            curY += (8 if sm else 12)
            curX = x
            continue
        if(char in (letters_sm if sm else letters_bg)):
            for ca in (letters_sm if sm else letters_bg)[char]:
                f(curX + ((ca >> 12) & 15) - 1, curY + ((ca >> 8) & 15) - 1, ((ca >> 4) & 15), (ca & 15))
        curX += (6 if sm else 10)


def dr_hover(x, y):
    f(x - 1, y - 1, 9, 2)
    f(x, y, 7, 2)
    f(x + 1, y + 1, 5, 2)
    f(x + 2, y + 2, 3, 2)

def clr_hover():
    d.set_color(118, 159, 151)
    dr_hover(*hovers[c_grp][c_ho[1]][c_ho[0]])
def up_hover(dx, dy):
    c_ho[1]  = max(0, min(c_ho[1] + dy, len(hovers[c_grp]) - 1))
    c_ho[0] = max(0, min(c_ho[0] + dx, len(hovers[c_grp][c_ho[1]]) - 1))
    d.set_color(255, 255, 255)
    dr_hover(*hovers[c_grp][c_ho[1]][c_ho[0]])

def dr_bg(sect = 0):
    d.set_color(118, 159, 151)
    f(-1, (-1 if sect == 0 else 140), 321, 211)

def draw_suit_icons():
    d.set_color(255, 255, 255)
    f(24, 117, 6, 11)
    f(33, 117, 6, 11)
    f(23, 118, 8, 9)
    f(32, 118, 8, 9)
    f(22, 119, 19, 7)
    f(25, 125, 13, 4)
    f(26, 128, 11, 2)
    f(27, 129, 9, 2)
    f(28, 130, 7, 2)
    f(29, 131, 5, 2)
    f(30, 132, 3, 2)
    f(94, 117, 3, 17)
    f(93, 118, 5, 15)
    f(92, 119, 7, 13)
    f(91, 120, 9, 11)
    f(90, 121, 11, 9)
    f(89, 122, 13, 7)
    f(88, 123, 15, 5)
    f(87, 124, 17, 3)
    f(157, 117, 5, 17)
    f(156, 118, 7, 5)
    f(155, 119, 9, 4)
    f(153, 122, 13, 8)
    f(152, 123, 15, 6)
    f(151, 124, 17, 4)
    f(222, 117, 3, 2)
    f(221, 118, 5, 16)
    f(220, 119, 7, 2)
    f(219, 120, 9, 2)
    f(218, 121, 11, 2)
    f(217, 122, 13, 2)
    f(216, 123, 15, 2)
    f(215, 124, 17, 5)
    f(216, 128, 15, 2)
    f(285, 122, 9, 12)
    f(284, 121, 2, 12)
    f(283, 120, 2, 12)
    f(293, 126, 2, 7)
    f(294, 127, 2, 5)
    f(295, 126, 2, 5)
    f(296, 125, 2, 5)
    f(297, 126, 2, 2)
    f(292, 121, 3, 4)
    f(294, 120, 2, 4)
    f(295, 121, 2, 2)
    f(287, 120, 5, 3)
    f(288, 119, 4, 2)
    f(289, 118, 4, 2)
    f(290, 117, 2, 2)
    f(282, 121, 2, 2)
    f(282, 124, 2, 5)
    f(281, 123, 2, 5)
    f(280, 124, 2, 2)
    f(282, 129, 2, 2)

    d.set_color(135, 72, 80)
    f(24, 118, 6, 9)
    f(33, 118, 6, 9)
    f(23, 119, 8, 7)
    f(32, 119, 8, 7)
    f(25, 120, 13, 8)
    f(26, 127, 11, 2)
    f(27, 128, 9, 2)
    f(28, 129, 7, 2)
    f(29, 130, 5, 2)
    f(30, 131, 3, 2)
    f(94, 118, 3, 15)
    f(93, 119, 5, 13)
    f(92, 120, 7, 11)
    f(91, 121, 9, 9)
    f(90, 122, 11, 7)
    f(89, 123, 13, 5)
    f(88, 124, 15, 3)

    d.set_color(76, 58, 58)
    f(157, 118, 5, 7)
    f(156, 119, 7, 4)
    f(152, 124, 15, 4)
    f(153, 123, 4, 2)
    f(162, 123, 4, 2)
    f(153, 127, 13, 2)
    f(158, 128, 3, 5)
    f(222, 118, 3, 15)
    f(221, 119, 5, 2)
    f(220, 120, 7, 2)
    f(219, 121, 9, 2)
    f(218, 122, 11, 2)
    f(217, 123, 13, 2)
    f(216, 124, 15, 5)

    d.set_color(112, 141, 119)
    f(287, 122, 4, 5)
    f(286, 124, 2, 4)
    f(285, 123, 2, 10)
    f(284, 122, 2, 10)
    f(288, 126, 2, 2)
    f(287, 128, 2, 2)
    f(289, 128, 2, 2)
    f(288, 129, 2, 2)
    f(290, 124, 2, 4)
    f(291, 123, 2, 10)
    f(290, 130, 2, 3)
    f(286, 130, 2, 3)
    f(292, 126, 2, 7)
    f(293, 127, 2, 5)
    f(284, 128, 2, 3)
    f(295, 127, 2, 3)
    f(296, 126, 2, 2)
    f(283, 129, 2, 2)
    f(281, 124, 2, 2)
    f(282, 125, 2, 3)
    f(283, 126, 2, 2)
    f(283, 121, 2, 2)
    f(288, 120, 3, 3)
    f(289, 119, 2, 2)
    f(290, 118, 2, 2)
    f(292, 122, 2, 3)
    f(293, 122, 2, 2)
    f(294, 121, 2, 2)

def dr_sel1():
    d.set_color(255,255,255)
    for x in range(5):
        for y in range(3):
            f(19 + (x * 64), 148 + (y * 23), 25, 13)
    d.set_color(0, 0, 0)
    for x in range(5):
        for y in range(3):
            num = (x + (5*y) + 1)
            if(num < 10 or (num > 10 and num < 15)):
                num = ("A" if num == 1 else num if num < 10 else "J" if num == 12 else "Q" if num == 13 else "K" if num == 14 else "")
                w_t(str(num), 28 + (x * 64), 150 + (y * 23), False)
    w_t("10", 279, 173, False)
    w_t("CAN", 23, 197, True)
    w_t("CON", 279, 197, True)

def dr_sel2():
    global sel_cards
    sel_cards = []
    d.set_color(255,255,255)
    for x in range(4):
        for y in range(3):
            if(y == 2 and (x == 1 or x == 2)):
                continue
            f(19 + (x * 64), 148 + (y * 23), 25, 13)
    a_s = [heart, diamond, club, spade]
    a_s.remove(cur_cards[0][1])
    sel_cards.append(([(2, a_s[0]), (2, a_s[1]), (2, a_s[2])] if cur_cards[0][0] == 2 else [(3, a_s[0]), (3, a_s[1]), (3, a_s[2])] if cur_cards[0][0] == 3 else [(4, a_s[0]), (4, a_s[1]), (4, a_s[2])] if cur_cards[0][0] == 4 else [(5, a_s[0]), (5, a_s[1]), (5, a_s[2])] if cur_cards[0][0] == 5 else []))
    sel_cards.append([(1, 0), (1,1), (1,2), (1,3)])
    dr_sel_cards()

def dr_sel3():
    global sel_cards
    sel_cards = []
    d.set_color(255,255,255)
    for x in range(4):
        for y in range(3):
            if(y == 2 and (x == 1 or x == 2)):
                continue
            f(19 + (x * 64), 148 + (y * 23), 25, 13)
    a_s = [heart, diamond, club, spade]
    a_s.remove(cur_cards[0][1])
    a_s.remove(cur_cards[1][1])
    sel_cards.append(([(2, a_s[0]), (2, a_s[1])] if cur_cards[0][0] == 2 else [(3, a_s[0]), (3, a_s[1])] if cur_cards[0][0] == 3 else []))
    dr_sel_cards()

def dr_sel4():
    global sel_cards
    sel_cards = []
    d.set_color(255,255,255)
    for x in range(4):
        for y in range(3):
            if(y == 2 and (x == 1 or x == 2)):
                continue
            f(19 + (x * 64), 148 + (y * 23), 25, 13)
    a_s = [heart, diamond, club, spade]
    a_s.remove(cur_cards[0][1])
    a_s.remove(cur_cards[1][1])
    a_s.remove(cur_cards[2][1])
    sel_cards.append([(2, a_s[0])])
    dr_sel_cards()

def dr_sel_cards():
    d.set_color(0, 0, 0)
    for i in range(len(sel_cards[0])):
        w_t(("h" if sel_cards[0][i][1] == heart else "d" if sel_cards[0][i][1] == diamond else "c" if sel_cards[0][i][1] == club else "s") + str(sel_cards[0][i][0]), 23 + (i * 64), 150, False)
    if(len(sel_cards) > 1):
        for i in range(len(sel_cards[1])):
            w_t(("h" if sel_cards[1][i][1] == heart else "d" if sel_cards[1][i][1] == diamond else "c" if sel_cards[1][i][1] == club else "s") + "A", 23 + (i * 64), 173, False)
    w_t("CAN", 23, 197, True)
    w_t("CON", 215, 197, True)

def clr_b_info():
    d.set_color(118, 159, 151)
    f(118, 22, 83, 11)

def up_b_info():
    clr_b_info()
    d.set_color(135, 72, 80)
    w_t(str(c_he), 119, 23, False)
    d.set_color(76, 58, 58)
    w_t(("h" if c_b[1] == heart else "d" if c_b[1] == diamond else "c" if c_b[1] == club else "s") + ("J" if c_b[0] == j else "Q" if c_b[0] == q else "K"), 151, 23, False)
    w_t(str(c_at), 183, 23, False)

def set_boss_stats():
    global c_he
    global c_at
    if(c_b[0] == j):
        c_he = 20
        c_at = 10
    elif(c_b[0] == q):
        c_he = 30
        c_at = 15
    elif(c_b[0] == k):
        c_he = 40
        c_at = 20

def con_atk():
    global c_b
    global sel_suit
    global c_at
    global c_he
    global c_rank
    global left_in_rank
    global cur_cards
    global negated
    base_dmg = 0
    suits = []
    for c in cur_cards:
        base_dmg += (c[0] if c[0] < j else 10 if c[0] == j else 15 if c[0] == q else 20)
        suits.append(c[1])
    if(spade in suits and (c_b[1] != spade or negated)):
        c_at -= base_dmg
    if(club in suits and (c_b[1] != club or negated)):
        base_dmg *= 2
    c_he -= base_dmg
    if(c_he <= 0):
        sel_suit = None
        c_b = None
        if(left_in_rank == 0):
            left_in_rank = 4
            c_rank += 1
        clr_b_info()
        negated = False
    else:
        up_b_info()
    cur_cards = []
    set_grp("Suits")
    dr_bg(1)

def set_grp(grp):
    global c_grp
    d.set_color(118, 159, 151)
    #dr_hover(*hovers[c_grp][c_ho[1]][c_ho[0]])
    clr_hover()
    c_grp = grp
    up_hover(0, 0)

dr_bg()
draw_suit_icons()
up_hover(0, 0)

while True:
    d.set_color(0, 0, 0)
    key = s.wait_key()
    clr_hover()
    up_hover((1 if key == 26 else -1 if key == 24 else 0), (-1 if key == 25 else 1 if key == 34 else 0))
    if(key == 105):
        if(c_grp == "Suits"):
            if(c_b is None):
                c_b = (c_rank, min(spade, c_ho[0]))
                left_in_rank -= 1
                set_boss_stats()
                up_b_info()
            else:
                if(c_ho[0] < 4):
                    set_grp("Sel1")
                    sel_suit = c_ho[0]
                    dr_sel1()
                else:
                    negated = True
                    set_grp("Suits")
                    dr_bg(1)
        elif(c_grp == "Sel1"):
            if(not (c_ho[0] == 0 and c_ho[1] == 2) and not (c_ho[0] == 4 and c_ho[1] == 2)):
                num = c_ho[0] + (c_ho[1] * 5) + (1 if c_ho[1] > 2 else 0)
                clr_hover()
                up_hover(-4, -4)
                cur_cards.append((num + 1, sel_suit))
                dr_bg(1)
                set_grp("Sel2")
                dr_sel2()
        elif(c_grp == "Sel2"):
            if(c_ho[1] != 2):
                cur_cards.append(sel_cards[c_ho[1]][c_ho[0]])
                clr_hover()
                up_hover(-4, -4)
                if(len(cur_cards) == 1):
                    dr_sel2()
                elif(len(cur_cards) == 2 and cur_cards[0][0] <= 3):
                    dr_sel3()
                elif(len(cur_cards) == 3 and cur_cards[0][0] <= 2):
                    dr_sel4()
                else:
                    con_atk()

        if(c_ho[1] == 2):
            if(c_ho[0] == 0):
                cur_cards = []
                sel_suit = None
                set_grp("Suits")
                dr_bg(1)
            elif(c_ho[0] == len(hovers[c_grp][c_ho[1]]) - 1):
                con_atk()




