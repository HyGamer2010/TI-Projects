import ti_draw as d
import ti_system as s
from ti_draw import fill_rect as f,set_color as s_co
from random import randrange as rr

c_js = []
c_h_js = []

c_s_j = None
c_m_j = None
c_m_j_index = 0

c_ho = [1, 0]

c_m = "shop"

b_c_a = [100, 300, 800, 2000, 5000, 11000, 20000, 35000, 50000]

mo = 4
t_h = 4
t_d = 4
h = 0
di = 0
c_r = 0
a = 0

c = 0
m = 0

sc = 0
n_sc = 0

c_ha = []
c_ha_t = 0
s_c = [False, False, False, False, False, False, False, False]
s_c_c = 0
n_c = []
su_c = []

r_c = 5

r_m = 3.00
se_rt = 10

ha_s = 8

c_d = []
for i in range(4):
    for j in range(1, 14):
        c_d.append([i, j])
t_de = [x[:] for x in c_d]

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

hover_pos = {
    "shop": [
        [(100,9),(130,9),(160,9),(190,9),(220,9)],
        [(122,113),(177,113),(207,113),(237,113)],
        [(122,159)]
    ],
    "blind": [
        [(100,9),(130,9),(160,9),(190,9),(220,9)],
        [(94,139),(120,139),(146,139),(172,139),
         (198,139),(224,139),(250,139),(276,139)],
        [(161,190),(209,190)]
    ]
}

hand_types = {
    1: ("STRAIGHT|FLUSH", 100, 8),
    2: ("FOUR OF A|KIND", 60, 7),
    3: ("FULL|HOUSE", 40, 4),
    4: ("|FLUSH", 35, 4),
    5: ("|STRAIGHT", 30, 4),
    6: ("THREE OF A|KIND", 30, 3),
    7: ("|TWO PAIR", 20, 2),
    8: ("|PAIR", 10, 2),
    9: ("|HIGH CARD", 5, 1)
}

hand_levels = {
    1: (40, 4),
    2: (30, 3),
    3: (25, 2),
    4: (15, 2),
    5: (30, 3),
    6: (20, 2),
    7: (20, 1),
    8: (15, 1),
    9: (10, 1)
}

blind_panels = {
    1: ((18,61,103), (1,102,170), "SMALL", (16, 39), "SMALL BLIND", (16, 15), 1),
    2: ((87,68,25), (165,109,0), "BIG", (22, 39), "BIG BLIND", (22, 15), 1.5),
    0: ((76,38,27), (151,36,5), "BOSS", (19, 39), "BOSS BLIND", (19, 15), 2)
}

j_info = {
    "Jimbo": ("JIMBO|+4 MULT|BUY $2 SELL $1", 2, 1, 0),
    "Blueprint": ("BLUEPRINT|COPIES ABILITY OF JOKER|TO THE RIGHT|BUY $10 SELL $5", 10, 5, 2),
    "Greedy": ("GREEDY JOKER|PLAYED CARDS WITH DIAMOND SUIT|GIVE +3 MULT WHEN SCORED|BUY $5 SELL $2", 5, 2, 0),
    "Lusty": ("LUSTY JOKER|PLAYED CARDS WITH HEART SUIT|GIVE +3 MULT WHEN SCORED|BUY $5 SELL $2", 5, 2, 0),
    "Wrathful": ("WRATHFUL JOKER|PLAYED CARDS WITH SPADE SUIT|GIVE +3 MULT WHEN SCORED|BUY $5 SELL $2", 5, 2, 0),
    "Gluttonous": ("GLUTTONOUS JOKER|PLAYED CARDS WITH CLUB SUIT|GIVE +3 MULT WHEN SCORED|BUY $5 SELL $2", 5, 2, 0),
    "Faceless": ("FACELESS JOKER|EARN $5 IF 3 OR MORE ROYALS|ARE DISCARDED AT THE SAME TIME|BUY $4 SELL $2", 4, 2, 0),
    "Golden": ("GOLDEN JOKER|EARN $4 AT END OF ROUND|BUY $6 SELL $3", 6, 3, 0),
    "Even": ("EVEN STEVEN|PLAYED CARDS WITH EVEN RANK GIVE|+4 MULT WHEN SCORED|BUY $4 SELL $2", 4, 2, 0),
    "Odd": ("ODD TODD|PLAYED CARDS WITH ODD RANK GIVE|+31 CHIPS WHEN SCORED|BUY $4 SELL $2", 4, 2, 0),
    "Swash": ("SWASHBUCKLER|ADDS THE SELL VALUE OF ALL OTHER OWNED|JOKERS TO MULT|BUY $4 SELL $2", 4, 2, 0),
    "Misprint": ("MISPRINT|+0-23 MULT|BUY $4 SELL $2", 4, 2, 0),
    "Half": ("HALF JOKER|+20 MULT IF PLAYED HAND CONTAINS|3 OR FEWER CARDS|BUY $5 SELL $2", 5, 2, 0),
    "Space": ("SPACE JOKER|1 IN 4 CHANCE TO UPGRADE| LEVEL OF PLAYED POKER HAND|BUY $5 SELL $2", 5, 2, 1),
    "Chad": ("HANGING CHAD|RETRIGGER FIRST PLAYED CARD USED|IN SCORING 2 ADDITIONAL TIMES|BUY $4 SELL $2", 4, 2, 0),
    "Photo": ("PHOTOGRAPH|FIRST PLAYED FACE CARD GIVES|X2 MULT WHEN SCORED|BUY $5 SELL $2", 5, 2, 0),
    "Sharp": ("CARD SHARP|X3 MULT IF PLAYED POKER HAND HAS|ALREADY BEEN PLAYED THIS ROUND|BUY $6 SELL $3", 6, 3, 1),
    "Boot": ("BOOTSTRAPS|+2 MULT FOR EVERY $5 YOU HAVE|BUY $7 SELL $3", 7, 3, 1),
    "Rocket": ("ROCKET|EARN $1 AT THE END OF ROUND. PAYOUT|INC BY $2 WHEN BOSS BLIND IS DEFEATED|BUY $6 SELL $3", 6, 3, 1),
    "Bull": ("BULL|+2 CHIPS FOR EACH $1 YOU HAVE|BUY $6 SELL $3", 6, 3, 1),
    "Ramen": ("RAMEN|X3 MULT.LOSES X0.01 MULT|PER CARD DISCARDED|BUY $6 SELL $3", 6, 3, 1),
    "Selt": ("SELTZER|RETRIGGER ALL CARDS PLAYED FOR|THE NEXT 10 HANDS|BUY $6 SELL $3", 6, 3, 1),
    "Gem": ("ROUGH GEM|PLAYED CARDS WITH DIAMOND SUIT|EARN $1 WHEN SCORED|BUY $7 SELL $3", 7, 3, 1),
    "Blood": ("BLOODSTONE|1/2 CHANCE FOR PLAYED CARDS WITH HEART|SUIT TO GIVE 1.5X MULT WHEN SCORED|BUY $7 SELL $3", 7, 3, 1),
    "Onyx": ("ONYX AGATE|PLAYED CARDS WITH CLUB SUIT|GIVE +7 MULT WHEN SCORED|BUY $7 SELL $3", 7, 3, 1),
    "Arrow": ("ARROWHEAD|PLAYED CARDS WITH SPADE SUIT|GIVE +50 CHIPS WHEN SCORED|BUY $7 SELL $3", 7, 3, 1),
    "Burnt": ("BURNT JOKER|UPGRADE THE LEVEL OF THE FIRST|DISCARDED POKER HAND EACH ROUND|BUY $8 SELL $4", 8, 4, 2),
    "Stunt": ("STUNTMAN|+250 CHIPS.-2 HAND SIZE|BUY $7 SELL $3", 7, 3, 2)
}

played_types = []

col = [
    0xFFFFFF,
    0x5B5B5B,
    0xFDA200,
    0xFD5F55,
    0x009CFD
]

def_p = [
        col[0],
        col[1],
        col[2],
        col[3],
        col[4],
        col[0],
        col[3],
        col[1],
        col[0],
        col[2],
        col[0]
    ]
swash_p = def_p.copy()
swash_p[1] = 0x4F6367
swash_p[3] = 0xA3895F
swash_p[4] = 0xEFE6D4
swash_p.pop()

odd_p = def_p.copy()
odd_p[3] = col[4]
odd_p[6] = 0x0282D4
odd_p[9] = 0x0282D4

even_p = def_p.copy()
even_p[2] = 0xA5605B
even_p[4] = col[3]

face_p = def_p.copy()
for i in range(6, 10):
    face_p[i] = col[0]

photo_p = def_p + [0x885D86, 0xA592A4, 0xD3B79A]
photo_p[7] = col[2]

burnt_p = def_p + [0xFDA857, col[1]]
burnt_p[2] = 0xFDCF51
burnt_p[4] = col[3]
burnt_p[6] = col[2]
burnt_p[7] = 0x98EDFE
burnt_p[9] = col[3]

palletes = {
    "Jimbo": def_p,
    "Wrathful": [
        0x5E579C,
        0x3E3790,
        0x3E3790,
        0x766FB5,
        0x8D88BA,
        col[0],
        0x766FB5,
        0x3E3790,
        col[0],
        0x3E3790,
        0x766FB5
    ],
    "Greedy": [
        0xD76B1C,
        0x814519,
        0x864C1B,
        0xF28B3C,
        0xF1AA75,
        0xFDEAD7,
        0xF48B3F,
        0xA05F28,
        0xFDEAD7,
        0x864C1B,
        0xF28B3C
    ],
    "Gluttonous": [
        0x00675D,
        0x00534B,
        0x00675D,
        0x207C74,
        0x1F847E,
        0xE8FFFF,
        0x439F97,
        0x00675D,
        0xE8FFFF,
        0x00675D,
        0x46A39A
    ],
    "Lusty": [
        0xEB2D32,
        0x9A0F11,
        0xA61B1E,
        0xFF6468,
        0xFE6269,
        0xFDE8EB,
        0xE6555D,
        0xA82027,
        0xFDE8EB,
        0xA82027,
        0xFE6269
    ],
    "Golden": [
        col[0],
        0x8C6721,
        0xCF9227,
        0xEFBD5E,
        0xF9C570,
        0xFFD896,
        0xD29329,
        0x977537,
        0xFFD896,
        0xD29329,
        0xD29329
    ],
    "Faceless": face_p,
    "Blueprint": [
        0x4C69CF,
        0xDBEEFF,
        0x6183F5,
        0x3E60D4,
        0x7F97EC,
        0xACBDF9,
        0x3F5FD3,
        0x435FBC,
        col[0],
        0x657CF1,
        0xACBDF9
    ],
    "Even": even_p,
    "Odd": odd_p,
    "Swash": swash_p,
    "Misprint": def_p,
    "Half": def_p,
    "Space": [
        col[0],
        0x4F6367,
        2,
        3,
        col[0],
        0x88A0A5,
        0x5E7579,
        col[1],
        0xA0B4B8,
        0x5D7477,
    ],
    "Chad": [
        0xF0F5F5,
        0x5D7477
    ],
    "Photo": photo_p,
    "Sharp": [
        col[0],
        col[1],
        0x61929B,
        0x4F6367,
        col[4],
        col[0],
        col[3],
        col[1],
        col[0],
    ],
    "Boot": [
        col[0],
        0xF8A065,
        col[1],
        0xBD9C66,
        0xD46F4E,
        0xD8D8D9
    ],
    "Rocket": [
        col[0],
        0x4F6367,
        col[3],
        0xBFC7D5,
        0x4895C5,
        0xFDA4A1,
        0xFDCE9D,
        0xF9EAB8,
        col[0]
    ],
    "Bull": [
        col[0],
        0x485E62,
        0x798C90,
        0xD3B9C7,
        0x7A687D,
        0xFDDF90
    ],
    "Ramen": [
        col[0],
        0xA95476,
        col[1],
        0xD7E2EB,
        0x0897D8,
        0xCA6430,
        0x398C52,
        0xF7DB77
    ],
    "Selt": [
        col[0],
        0x6172D9,
        col[1],
        0xACD9F9,
        0xDDEAF9,
        0x627A92,
        0xB2BECA
    ],
    "Gem": [
        col[0],
        0xF6DCB1,
        0x7EAAB2,
        0xA0E6F6
    ],
    "Blood": [
        col[0],
        0xFCE7E8,
        0x5C9185,
        0x94C5BB,
        0xC5492F
    ],
    "Onyx": [
        col[0],
        0xBED9EC,
        0x4F6367,
        0xEFF8F9
    ],
    "Arrow": [
        col[0],
        0xE2E0FA,
        0x36777D,
        0x588995
    ],
    "Burnt": burnt_p,
    "Stunt": [
        col[0],
        col[1],
        0x009CFD,
        col[2],
        4,
        5,
        col[3],
        7,
        col[0]
    ]
}

jimbo_spr = "0,1,2,3,4,5,6,7,8,9,10"
jimbo_vars = ["Jimbo", "Wrathful", "Greedy", "Lusty", "Gluttonous", "Golden", "Faceless", "Blueprint"]

j_sprs = {name: jimbo_spr for name in jimbo_vars }
j_sprs["Even"] = "0,11,12,13,4,5,6,7,8,14,15,10"
j_sprs["Odd"] = "0,16,3,4,5,6,7,8,9,10"
j_sprs["Swash"] = "0,17,18,4,5,6,7,8,9,19"
j_sprs["Misprint"] = jimbo_spr + ",20,21,22,23,24"
j_sprs["Half"] = "0,1,2,3,4,5,6,7,8,9,10,25"
j_sprs["Space"] = "0,26,4,5,6,7,8,9,27"
j_sprs["Chad"] = "0,28,29"
j_sprs["Photo"] = "30,31,32,33,1,2,3,4,5,6,7,8,9,10"
j_sprs["Sharp"] = "0,34,4,5,6,8,35,36"
j_sprs["Boot"] = "0,37,38,39,40,41"
j_sprs["Rocket"] = "0,37,42,43,44,45,46,47,48"
j_sprs["Bull"] = "0,49,50,51,52,53,54,55"
j_sprs["Ramen"] = "0,37,56,57,58,59,60,61"
j_sprs["Selt"] = "0,37,62,63,64,65,66"
j_sprs["Gem"] = "0,37,67,68"
j_sprs["Blood"] = "0,37,69,70,71"
j_sprs["Onyx"] = "0,37,72,73"
j_sprs["Arrow"] = "0,37,74,75"
j_sprs["Burnt"] = "0,76,1,2,3,4,5,6,7,8,9,10,77"
j_sprs["Stunt"] = "0,78,79,6,8,80,81,82"

sprs = {
    0: [
        0,
        394537,
        7843,
        134695,
    ],
    1: [
        1,
        1192479,
        695305,
        811921,
        975618,
        572547,
        1071765,
        2240644,
        2109573,
        1321474,
        1450370,
        1579266,
        2382086,
        2646214,
        2779334,
        3045509,
        2789506,
        2922626,
        678022,
        546948,
        417990,
        288966,
        161925,
        430210,
        301186,
        850821,
        2425029,
        2558150,
        2822275,
        721093,
        592070,
        462979,
        1253570,
        1124547,
        1908930,
        2042051
    ],
    2: [
        2,
        813956,
        2384132,
        549124,
        2779269,
        2914435,
        419973,
        292995,
    ],
    3: [
        3,
        825477,
        2398341,
        948359,
        2259079,
        1075400,
        1992904,
        1202697,
        1323398,
        1452419,
        1581314,
        2109570
    ],
    4: [
        4,
        1112708,
        1249794,
        1382530,
        1906818,
        852867,
        723139,
        2427075,
        594115,
        2560195
    ],
    5: [
        5,
        1350030,
        1221132,
        1094280,
        703491,
        838531,
        973570
    ],
    6: [
        6,
        1101955,
        2150531,
        1233028,
        2019460,
        1366404
    ],
    7: [
        7,
        1095874,
        2013378
    ],
    8: [
        8,
        1235074,
        2021506,
        1368450
    ],
    9: [
        9,
        1089667,
        2138243,
        960644,
        2271364,
        1222786,
        2009218,
        1355907,
        1880195,
        1097922,
        2015426
    ],
    10: [
        10,
        2113666,
        299138,
        2920578
    ],
    11: [
        1,
        695305,
        572547,
        813968,
        942482,
        1728914,
        547270,
        1989062,
        417990,
        2646214,
        288967,
        2779335,
        161925,
        3045509,
        301186,
        2922626,
        1106568,
        850821,
        721093,
        2425029,
        592070,
        2558150,
        462979,
        2822275,
        1251842,
        1253570,
        1908930,
        1124547,
        2042051
    ],
    12: [
        2,
        1730951,
        1603714,
        1607810,
        2005314,
        2269378,
        2402435,
        1990981,
        2515140,
        2779269,
        2914435
    ],
    13: [
        3,
        944519,
        1601666,
        1605762,
        1609858,
        825666,
        827586,
        424067,
        811333,
        549060,
        419973,
        292995
    ],
    14: [
        3,
        2138243,
        2271364,
        2009218,
        1880195,
        2015426
    ],
    15: [
        2,
        1089667,
        960644,
        1222786,
        1355907,
        1097922
    ],
    16: [
        1,
        1071769,
        1192479,
        944913,
        818062,
        695305,
        572547,
        1321478,
        2240644,
        1450370,
        1579266,
        850821,
        721093,
        2425029,
        592070,
        2558150,
        462979,
        2822275,
        1253570,
        1908930,
        1124547,
        2042051
    ],
    17: [
        1,
        942866,
        813968,
        685070,
        572547,
        556167,
        427271,
        298373,
        169476,
        40578,
        1071449,
        1726809,
        1239560,
        850821,
        721093,
        2425029,
        592070,
        2558150,
        462979,
        2822275,
        1200348,
        1855708,
        1124547,
        2042051
    ],
    18: [
        3,
        944902,
        815430,
        1995078,
        686342,
        686342,
        2259206,
        557318,
        2654470,
        428165,
        2787461,
        299139,
        2920579,
        170114,
        3053698,
        698498,
        2533506,
        1073474,
        1728834,
        1202370,
        1857730
    ],
    19: [
        1,
        1878277,
        1749379,
        1745026,
        1611906,
        2408578
    ],
    20: [
        1,
        2173571,
        2167426,
        2157187,
        2144898,
        2120323,
        2116226,
        2112130,
        2108034
    ],
    21: [
        3,
        2151043,
        2124424,
        2110082
    ],
    22: [
        10,
        2114178,
        2118274,
        2142850,
        2148995,
        2155138,
        2169475
    ],
    23: [
        9,
        2146946,
        2138755
    ],
    24: [
        4,
        2161284
    ],
    25: [
        -1,
        55566,
        450765,
        714956,
        979147,
        1243338,
        1503499,
        1895180,
        2286146,
        2676994
    ],
    26: [
        1,
        816017,
        944919,
        1073794,
        1333658,
        687119,
        558221,
        429323,
        302471,
        418118,
        536775,
        407875,
        1251523,
        1906883,
        850821,
        721093,
        2425029,
        592070,
        2558150,
        1124547,
        2042051,
        462979,
        2822275
    ],
    27: [
        4,
        977026,
        2287746,
        843906,
        2416770,
        710786,
        2545794,
        575619,
        2672771,
        432263,
        2791559,
        559236,
        2656388,
        688259,
        2523267,
        817283,
        2390147,
        946307,
        2257027,
        1075395,
        1992899,
        1335683,
        548997,
        680068,
        538819
    ],
    28: [
        1,
        266370,
        396546,
        2887810,
        3020963,
        2959490,
        472322,
        338050,
        180366,
        43140,
        313602,
        705474,
        2410630,
        837766,
        977666,
        1493251,
        1497219,
        1630402,
        833666,
        963394,
        1091714,
        1220738,
        301186,
        430210,
        559234,
        688258,
        817282,
        1341570,
        946434,
        1474695,
        1349890,
        1608194,
        2396293,
        1740930,
        1745027,
        793538,
        2367622,
        794758,
        934658,
        1450242,
        1583236,
        1456258,
        850818,
        852102,
        2424966,
        992002,
        1507461,
        1638594,
        1771650,
        1642626,
        1775746,
        137363
    ],
    29: [
        -1,
        807813,
        815234,
        1340034,
        1342082
    ],
    30: [
        0,
        1705
    ],
    31: [
        11,
        134679
    ],
    32: [
        12,
        179722
    ],
    33: [
        13,
        198152
    ],
    34: [
        1,
        462088,
        333190,
        558226,
        431374,
        304523,
        685059,
        813954,
        942850,
        1202690
    ],
    35: [
        2,
        463494,
        1774214,
        592450,
        1772098,
        721218,
        721218,
        2163010,
        716931,
        2551939,
        583811,
        2680963,
        434315,
        2793611,
        561286,
        2658438,
        688263,
        2523271,
        815240,
        2388104,
        944264,
        2254984,
        1075399,
        1992903,
        1204743
    ],
    36: [
        3,
        1092227,
        962947,
        1749379,
        1097986,
        1884418
    ],
    37: [
        1,
        396583,
        267685,
        138659
    ],
    38: [
        2,
        1477267,
        2169154,
        1374470,
        721285,
        587973,
        456836
    ],
    39: [
        3,
        1610256,
        1505668,
        1376516,
        723331,
        590019
    ],
    40: [
        4,
        1767620,
        1634436,
        1505410,
        1974420,
        1845517,
        1716612,
        1587715,
        1458818
    ],
    41: [
        5,
        2161218,
        2551940,
        2814084,
        2680962,
        2943106,
        2689154,
        2951298,
        3076226,
        3080322
    ],
    42: [
        2,
        693257,
        565448,
        2531528,
        579716,
        2676868,
        934658,
        1190403,
        1319298,
        1448194,
        1577090
    ],
    43: [
        3,
        936722,
        813964,
        1102466,
        1235460,
        1110658,
        981762,
        852738
    ],
    44: [
        4,
        1470726,
        1341828
    ],
    45: [
        5,
        1116806,
        1126530,
        2175106,
        1388930
    ],
    46: [
        6,
        1247748,
        1384834,
        1648770
    ],
    47: [
        7,
        1378691,
        1513730
    ],
    48: [
        8,
        1509634,
        1642626,
        1063554
    ],
    49: [
        1,
        678926,
        836483,
        971526,
        1112706,
        290183,
        155847,
        2908359,
        26757,
        3172485,
        534791,
        2369799,
        938114,
        2248834,
        663811,
        2236675,
        1056898,
        2105474,
        792770,
        2234562
    ],
    50: [
        2,
        811917,
        967427,
        292229,
        157893,
        2910405
    ],
    51: [
        3,
        1102470
    ],
    52: [
        4,
        1237187,
        1892547
    ],
    53: [
        5,
        809154,
        2250946,
        676034,
        2379970,
        667781,
        2502789,
        665794,
        2369730,
        794818,
        2236610
    ],
    54: [
        0,
        954563,
        2134211
    ],
    55: [
        1,
        1218690,
        1085570,
        952450,
        2005122,
        2134146,
        2263170
    ],
    56: [
        2,
        697354,
        568454,
        846723,
        981762,
        1114754,
        1247746
    ],
    57: [
        3,
        698502,
        2533510,
        1235463,
        1104518,
        970950,
        2150598,
        839812,
        2412676
    ],
    58: [
        4,
        841922,
        2283714,
        1106562
    ],
    59: [
        5,
        827844,
        961285,
        1231362,
        2396355
    ],
    60: [
        6,
        1335561,
        1075402,
        1224834,
        815302,
        956546,
        686211,
        1734918,
        1606022,
        1747138,
        2265219
    ],
    61: [
        7,
        952452,
        1208456,
        1740933,
        1998982,
        1607810,
        1081666,
        1472706,
        1730691,
        1861764,
        1331334,
        1077378,
        813250,
        680066,
        540805,
        1990786,
        1597570,
        1458309,
        2117763,
        2242692,
        1198210,
        1065090,
        929923,
        794755,
        1585283,
        1714306
    ],
    62: [
        2,
        822159,
        949013,
        1077911,
        1202692,
        1327621,
        2246787,
        932484,
        802947,
        938115,
        1192386,
        1452290
    ],
    63: [
        3,
        957197,
        1112709
    ],
    64: [
        4,
        953091,
        1079939,
        1208834,
        1468674
    ],
    65: [
        5,
        1599638,
        1333379,
        1857667,
        1454343,
        1849475,
        1982595,
        2115715
    ],
    66: [
        6,
        1194179,
        934083
    ],
    67: [
        2,
        695236,
        955081,
        832387,
        1214924,
        1102466,
        1368450,
        1474767,
        2531459,
        2277507,
        2021506,
        1892482,
        1763458,
        1634434,
        1116420,
        987522,
        1245314,
        2162884,
        2291971,
        2427010,
        809157,
        680259,
        2118086,
        2246920,
        1991235,
        2375939,
        2504834,
        1988738,
        1859714
    ],
    68: [
        3,
        1088136,
        959237,
        1216970,
        1476813,
        828291,
        1366402,
        956546,
        2019458,
        1761410,
        1632386,
        1118466,
        1247362,
        2293891,
        2424962,
        811203,
        2120068,
        2248966,
        2777219,
        2377922,
        1990786,
        2642050,
        2506882
    ],
    69: [
        2,
        1207175,
        1331920,
        1589653,
        1460816,
        1204880,
        2644108,
        1077840,
        950413,
        823434,
        698501,
        1239490,
        1503490,
        852227,
        981125,
        1118338,
        1247362,
        2420998,
        2292100,
        927941,
        799043,
        2105731,
        2238851,
        2234562,
        2504898,
        2410626
    ],
    70: [
        3,
        1462864,
        1591699,
        1335887,
        1208847,
        2513036,
        2648199,
        1081485,
        954506,
        829573,
        1237442,
        1501442,
        983171,
        1116290,
        2423044,
        929987,
        2236611,
        2500803
    ],
    71: [
        4,
        1233026,
        1628290,
        1601666,
        1998978,
        2392194,
        1988738,
        2142404,
        2013315,
        1611972,
        1749122,
        1876098,
        1218691,
        1089667,
        1353859,
        1224835
    ],
    72: [
        2,
        1084101,
        1223234,
        1356226,
        1489218,
        1213058,
        1341954,
        1470850,
        1599746,
        2371783,
        2242885,
        2113987,
        798918,
        1060997,
        670083,
        673922,
        2150596,
        2021507,
        2156674,
        2414722,
        972998,
        1235077,
        844163,
        714882,
        848002,
        1101954
    ],
    73: [
        3,
        972930,
        843906,
        714882,
        848002,
        981122,
        1353858,
        1482882,
        1611906,
        1994882,
        2244738,
        2377858,
        2510978,
        1083586,
        1343810,
        1738883,
        2128007,
        2009219
    ],
    74: [
        2,
        1110659,
        1204755,
        1079951,
        1331587,
        1460482,
        1589378,
        957189,
        834438,
        985285,
        856387,
        2298118,
        2169220,
        2660548,
        2531458,
        2924675,
        2797698,
        663878,
        792776,
        534979,
        1194114,
        1067138,
        938114
    ],
    75: [
        3,
        1241602,
        1370498,
        1462548,
        1335684,
        1210894,
        965381,
        1088133,
        1591426,
        794822,
        665731,
        1058948,
        936066,
        2662594,
        2795650,
        987331,
        2300164
    ],
    76: [
        11,
        396583,
        267685,
        138659
    ],
    77: [
        12,
        393538,
        792963,
        1179906,
        1312962,
        1183938,
        2885830,
        3152022,
        2752644,
        2621571,
        2359490,
        2631940,
        2498755,
        2769154,
        667844,
        803076,
        940162,
        192771,
        321987,
        581890,
        71811,
        204996,
        471235,
        735682
    ],
    78: [
        1,
        460037,
        588935,
        732162,
        865154,
        942877,
        683025,
        846722,
        554127,
        425229,
        298378
    ],
    79: [
        0,
        1120902,
        987526,
        1773958,
        854406,
        1902982,
        721222,
        2163014,
        589957,
        2687109,
        957186,
        828290,
        702723,
        2275587,
        1487111,
        836484,
        973570,
        831618,
        2404482,
        1357954,
        1882242,
        1106562,
        1239555,
        1374594,
        977026,
        2287746,
        843906,
        2416770,
        710786,
        2545794,
        577666,
        2674818,
        428170,
        2787466,
        555141,
        2652293,
        685061,
        944899
    ],
    80: [
        2,
        1468678,
        1124548,
        2042052,
        989379,
        2169027,
        856258,
        2298050,
        723138,
        2427074,
        590018,
        2556098
    ],
    81: [
        6,
        1206406,
        1992838,
        1517700,
        1779844,
        1382531,
        1906819,
        1249410,
        2035842,
        1116290,
        2164866,
        983170,
        2293890
    ],
    82: [
        3,
        817282,
        688258,
        2390146,
        2523266,
        592002,
        2689154,
        725122,
        2560130,
        858243,
        2431107,
        993411,
        2304131,
        944259,
        2254979,
        428226,
        2656450
    ]
}

def rgb(c):
    return ((c >> 16) & 255), ((c >> 8) & 255), (c & 255)

def dr_background():
    #Green backgc_r color
    s_co(59, 117, 93)
    f(-1, -1, 13, 241)
    f(84, -1, 3, 241)
    f(86, 63, 234, 177)
    f(86, -1, 156, 15)
    f(241, -1, 79, 65)

def dr_banner():
    #Gray shop menu color
    s_co(44, 58, 61)
    f(13, -1, 70, 211)

    #Red outline menu color
    s_co(193, 90, 81)
    f(11, -1, 3, 241)
    f(82, -1, 3, 241)

    s_co(0, 147, 253)#chip blue
    f(14, 89, 68, 12)

    s_co(255, 73, 64)#red button
    f(14, 108, 68, 12)
    f(41, 101, 5, 3)
    f(41, 105, 5, 3)
    f(50, 101, 5, 3)
    f(50, 105, 5, 3)
    f(45, 102, 3, 5)
    f(48, 102, 3, 5)
    f(47, 103, 2, 3)

    #White
    s_co(255, 255, 255)
    d.fill_circle(20, 67, 4)
    w_t("HANDS", 17, 170)
    w_t("DISCARDS", 17, 180)
    w_t("ROUND", 17, 190)
    w_t("ANTE", 17, 200)

def dr_shop_panel():
    s_co(193, 90, 81)#red outline
    f(86, 105, 184, 105)

    s_co(44, 58, 61)#gray
    f(88, 107, 180, 103)

    s_co(255, 73, 64)#red button
    f(95, 117, 62, 40)

    s_co(52, 189, 133)#green button
    f(95, 163, 62, 40)

    s_co(255, 255, 255)#white
    w_t("NEXT", 115, 133)
    w_t("REROLL", 109, 179)

    #banner sign
    s_co(193, 90, 81)#red outline
    f(16, 12, 64, 50)
    
    s_co(44, 58, 61)#gray
    f(18, 14, 60, 46)
    
    s_co(255, 73, 64)#red button color
    f(22, 23, 52, 28)

    s_co(255, 125, 119)#light red
    f(25, 23, 4, 28)
    f(31, 23, 4, 28)
    f(37, 23, 4, 28)
    f(43, 23, 4, 28)
    f(49, 23, 4, 28)
    f(55, 23, 4, 28)
    f(61, 23, 4, 28)
    f(67, 23, 4, 28)
    f(22, 26, 52, 4)
    f(22, 32, 52, 4)
    f(22, 38, 52, 4)
    f(22, 44, 52, 4)
    
    s_co(44, 58, 61)#gray
    f(25, 26, 46, 22)

    s_co(247, 209, 136)#shop letters
    f(28, 29, 8, 4)
    f(28, 35, 7, 4)
    f(27, 41, 8, 4)
    f(27, 30, 4, 8)
    f(32, 36, 4, 8)
    f(38, 29, 4, 16)
    f(38, 35, 9, 4)
    f(43, 29, 4, 16)
    f(49, 29, 4, 16)
    f(54, 29, 4, 16)
    f(49, 29, 9, 4)
    f(49, 41, 9, 4)
    f(60, 29, 4, 16)
    f(60, 29, 9, 4)
    f(60, 34, 9, 4)
    f(65, 29, 4, 9)

    s_co(255, 255, 255)
    if(c_r % 3 == 1):
        blind_text = "SMALL BLIND"
    elif(c_r % 3 == 2):
        blind_text = "BIG BLIND"
    elif(c_r % 3 == 0):
        blind_text = "BOSS BLIND"
    w_t("UPCOMING|" + blind_text, 245, 14)

def dr_blind_panel():
    bg, coin, label, label_pos, title, title_pos, multi = blind_panels[c_r % 3]

    s_co(*bg)
    f(13, 23, 70, 38)
    up_n_sc(round(b_c_a[a] * multi), *bg)

    s_co(*coin)
    d.fill_circle(30, 42, 16)
    f(13, 12, 70, 12)

    s_co(255, 255, 255)
    w_t(label, *label_pos)
    w_t(title, *title_pos)
    w_t("SCORE", 47, 34)

def cl_panel():
    s_co(44, 58, 61)#gray
    f(86, 105, 184, 105)
    f(13, 4, 70, 60)

def up_c_r(new_c_r):
    global c_r
    c_r = new_c_r

    s_co(44, 58, 61)
    f(50, 189, 6, 8)

    s_co(247, 185, 72)#gold
    w_t(str(c_r), 51, 190)

def up_a(new_a):
    global a
    a = new_a

    s_co(44, 58, 61)
    f(44, 199, 6, 8)

    s_co(247, 185, 72)#gold
    w_t(str(a), 45, 200)

def up_c(new_c):
    global c
    c = new_c

    s_co(0, 147, 253)
    f(16, 91, 66, 8)

    s_co(255, 255, 255)
    w_t(str(c), 17, 92)

def up_m(new_m):
    global m
    m = new_m

    s_co(255, 73, 64)
    f(16, 110, 66, 8)

    s_co(255, 255, 255)
    w_t(str(round(m)), 17, 111)

def up_di(new_di):
    global di
    di = new_di

    s_co(44, 58, 61)
    f(68, 179, 6, 8)

    s_co(255, 73, 64)#red button
    w_t(str(di), 69, 180)

def up_h(new_h):
    global h
    h = new_h

    s_co(44, 58, 61)
    f(50, 169, 6, 8)

    s_co(0, 147, 253)#chip blue
    w_t(str(h), 51, 170)

def up_sc(new_sc):
    global sc
    sc = new_sc

    s_co(44, 58, 61)
    f(25, 63, 58, 8)
    
    s_co(255, 255, 255)
    w_t(str(round(sc)), 26, 64)

def up_n_sc(new_n_sc, r, g, b):
    global n_sc
    n_sc = new_n_sc

    s_co(r, g, b)
    f(46, 43, 37, 8)

    s_co(255, 255, 255)
    w_t(str(n_sc), 47, 44)

def up_mo(new_mo):
    global mo
    mo = new_mo
    s_co(44, 58, 61)#gray
    f(163, 195, 101, 8)

    s_co(247, 185, 72)#gold
    w_t("$" + str(mo), 164, 196)

def up_hand_type(type : int):
    global c_ha_t
    c_ha_t = type

    s_co(44, 58, 61)
    f(16, 72, 67, 16)

    s_co(255, 255, 255)

    text, c, m = hand_types.get(type, ("", 0, 0))

    w_t(text, 17, 73)
    up_c(c)
    up_m(m)

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
                f(curX + ((ca >> 12) & 15) - 1, curY + ((ca >> 8) & 15) - 1, ((ca >> 4) & 15), (ca & 15))

        curX += 6

def dr_jkr_desc(text : str):
    lineSplit = text.split("|")
    maxX = 0
    maxY = len(lineSplit)
    for line in lineSplit:
        if(len(line) > maxX):
            maxX = len(line)
    s_co(255, 255, 255)
    f(86, 65, (maxX * 5) + (maxX - 1) + 5, (maxY * 7) + (maxY - 1) + 5)

    s_co(0, 0, 0)
    w_t(text, 89, 68)

def jkr_desc_sel(joker):
    if("Blueprint" in joker):
        dr_jkr_desc(j_info.get("Blueprint")[0])
    else:
        dr_jkr_desc(j_info.get(joker)[0])

def cl_joker_description():
    global c_s_j 
    c_s_j = None
    s_co(59, 117, 93)
    f(86, 65, 300, 40)
    
def dr_j_spr(x, y, sprite, pallete):
    for i in [int(j) for j in sprite.split(",")]:
        dr_spr(x, y, sprs[i], pallete, True)
        
def dr_spr(x, y, spr, pallete, isj = False):
    if(spr[0] == -1):
        if(c_ho[1] == 0):
            s_co(51, 92, 86)
        else:
            s_co(60, 81, 86)
    else:
        s_co(*rgb(pallete[spr[0]]))
    for i in range(len(spr) - 1):
        #ox, oy, w, h = spr[i + 1]
        f(x + abs((spr[i + 1] >> (17 if isj else 25)) & (31 if isj else 511)) - 1, y + abs((spr[i + 1] >> (11 if isj else 17)) & (63 if isj else 255)) - 1, abs((spr[i + 1] >> (6 if isj else 8)) & (31 if isj else 511)), abs(spr[i + 1] & (63 if isj else 255)))

def dr_joker(index, row):
    if(row == 0):
        xPos = index * 30 + 92
        yPos = 19
        if(c_js[index] is not None):
            joker = c_js[index]
        else:
            return
    elif(row == 1):
        xPos = index * 30 + 169
        yPos = 123
        if(c_h_js[index] is not None):
            joker = c_h_js[index]
        else:
            return

    if("Blueprint" in joker):
        dr_j_spr(xPos, yPos, j_sprs["Blueprint"], palletes["Blueprint"])
    else:
        dr_j_spr(xPos, yPos, j_sprs[joker], palletes[joker])
    
def dr_held_jokers():
    #Green shadow behind jokers at top
    s_co(51, 92, 86)
    f(86, 13, 156, 51)
    for i in range(len(c_js)):
        dr_joker(i, 0)

def dr_shop_jokers():
    #Buy joker area
    s_co(60, 81, 86)
    f(163, 117, 96, 51)
    for i in range(len(c_h_js)):
        dr_joker(i, 1)

def remove_hovered_joker():
    if(c_ho[1] == 0):
        xPos = c_ho[0] * 30 + 91
        yPos = 18
        s_co(51, 92, 86)
    elif(c_ho[1] == 1):
        xPos = (c_ho[0] - 1) * 30 + 168
        yPos = 122
        s_co(60, 81, 86)
    else:
        return
    f(xPos, yPos, 26, 41)
    cl_joker_description()

#24 = left, 25 = Up, 26 = right, 34 = down
def change_hover(input):
    cl_hover_redical()
    if(input == 25):
        c_ho[1] -= 1
    elif(input == 26):
        c_ho[0] += 1
    elif(input == 24):
        c_ho[0] -= 1
    elif(input == 34):
        c_ho[1] += 1
    if(c_ho[1] < 0):
            c_ho[1] = 0
    if(c_ho[0] < 0):
            c_ho[0] = 0
    if(c_m == "shop"):
        if(c_ho[1] > 2):
            c_ho[1] = 2
        if(c_ho[1] == 0 and c_ho[0] > 4):
            c_ho[0] = 4
        elif(c_ho[1] == 1 and c_ho[0] > 3):
            c_ho[0] = 3
        elif(c_ho[1] == 2 and c_ho[0] > 0):
            c_ho[0] = 0
    if(c_m == "blind"):
        if(c_ho[1] > 2):
            c_ho[1] = 2
        if(c_ho[1] == 0 and c_ho[0] > 4):
            c_ho[0] = 4
        elif(c_ho[1] == 1 and c_ho[0] > 7):
            c_ho[0] = 7
        elif(c_ho[1] == 2 and c_ho[0] > 1):
            c_ho[0] = 1

def dr_hover_redical(x, y):
    s_co(255, 255, 255)
    f(-1 + x, -1 + y, 8, 2)
    f(0 + x, 0 + y, 6, 2)
    f(1 + x, 1 + y, 4, 2)
    f(2 + x, 2 + y, 2, 2)

def cl_hover_redical():
    global c_m_j_index
    global c_ho
    if(c_ho[0] == c_m_j_index and c_m_j is not None):
        return
    x, y = hover_pos[c_m][c_ho[1]][c_ho[0]]

    s_co(*((44,58,61) if (c_m == "shop" and c_ho[1] > 0) else (59,117,93)))

    f(x, y, 8, 5)

def up_hover_redical():
    x, y = hover_pos[c_m][c_ho[1]][c_ho[0]]

    if(c_ho[1] == 1):
        cl_move_redical()
    dr_hover_redical(x + 1, y + 1)
    cl_joker_description()

def up_card_select_redical(index):
    offset = index * 26
    if(s_c[index]):
        s_co(51, 92, 86)
    else:
        s_co(59, 117, 93)
    f(85 + offset, 181, 2, 6)
    f(86 + offset, 183, 3, 6)
    f(88 + offset, 184, 21, 6)
    f(110 + offset, 181, 2, 6)
    f(108 + offset, 183, 3, 6)

def check_bp(bp_ind):
    if(bp_ind + 1 < len(c_js)):
        c_js[bp_ind] = "Blueprint:" + c_js[bp_ind + 1]
    
def buy_joker():
    global mo
    global se_rt
    if("Blueprint" in c_s_j):
        cost = j_info.get("Blueprint")[1]
    else:
        cost = j_info.get(c_s_j)[1]
    if(mo >= cost):
        length = len(c_js)
        index = c_ho[0] - 1
        c_h_js.pop(index)
        c_js.append(c_s_j)
        dr_joker(length, 0)
        if("Seltzer" in c_js[length]):
            se_rt = 10
        elif("Stunt" in c_js[length]):
            ha_s -= 2
        if("Blueprint" in c_js[length - 1]):
            check_bp(length - 1)
        
        dr_shop_jokers()
        up_mo(mo - cost)
        cl_joker_description()

def sell_joker():
    global mo
    global c_s_j
    global ha_s
    if("Blueprint" in c_s_j):
        sell_value = j_info.get("Blueprint")[2]
    else:
        sell_value = j_info.get(c_s_j)[2]
    if(c_s_j == "Stunt"):
        ha_s += 2
    up_mo(mo + sell_value)
    c_js.pop(c_ho[0])
    if(len > 1):
        if("Blueprint" in c_js[c_ho[0] - 1]):
            check_bp(c_ho[0] - 1)
    dr_held_jokers()
    cl_joker_description()

def dr_spadeclub(x, y, flip):
    if(not flip):
        f(x, -1 + y, 2, 2)
        f(-1 + x, y, 4, 2)
        f(x, 1 + y, 2, 2)
        f(-1 + x, 2 + y, 4, 2)
    else:
        f(x, 2 + y, 2, 2)
        f(-1 + x, 1 + y, 4, 2)
        f(x, y, 2, 2)
        f(-1 + x, -1 + y, 4, 2)

def dr_heart(x, y, flip):
    if(not flip):
        f(-1 + x, -1 + y, 2, 4)
        f(x, y, 2, 4)
        f(1 + x, -1 + y, 2, 4)
    else:
        f(-1 + x, y, 2, 4)
        f(x, -1 + y, 2, 4)
        f(1 + x, y, 2, 4)

def dr_diamond(x, y):
        f(-1 + x, y, 2, 3)
        f(x, -1 + y, 2, 5)
        f(1 + x, y, 2, 3)

def dr_card(suit : int, rank : int, x, y):
    s_co(255, 255, 255)#white
    f(2 + x, -1 + y, 20, 41)
    f(-1 + x, 2 + y, 26, 35)
    f(x, y, 24, 39)

    if(suit == 0):#spades
        s_co(0, 0, 0)
    elif(suit == 1):#clubs
        s_co(0, 147, 253)
    elif(suit == 2):#hearts
        s_co(255, 73, 64)
    elif(suit == 3):#diamonds
        s_co(247, 185, 72)

    
    if(rank == 2):
        positions = [[11, 5], [11, 30]]
        flip_range = 0

        f(1 + x, 1 + y, 4, 2)
        f(1 + x, 3 + y, 4, 2)
        f(1 + x, 5 + y, 4, 2)
        f(3 + x, 1 + y, 2, 4)
        f(1 + x, 3 + y, 2, 4)
    elif(rank == 3):
        positions = [[11, 5], [11, 17], [11, 30]]
        flip_range = 1

        f(1 + x, 1 + y, 4, 2)
        f(1 + x, 3 + y, 4, 2)
        f(1 + x, 5 + y, 4, 2)
        f(3 + x, 1 + y, 2, 6)
    elif(rank == 4):
        positions = [[8, 5], [14, 5], [8, 31], [14, 31]]
        flip_range = 1

        f(3 + x, 1 + y, 2, 6)
        f(1 + x, 1 + y, 2, 4)
        f(1 + x, 3 + y, 4, 2)
    elif(rank == 5):
        positions = [[8, 5], [14, 5], [11, 17], [8, 31], [14, 31]]
        flip_range = 2

        f(1 + x, 1 + y, 4, 2)
        f(1 + x, 3 + y, 4, 2)
        f(1 + x, 5 + y, 4, 2)
        f(1 + x, 1 + y, 2, 4)
        f(3 + x, 3 + y, 2, 4)
    elif(rank == 6):
        positions = [[8, 5], [14, 5], [8, 17], [14, 17], [8, 31], [14, 31]]
        flip_range = 3

        f(1 + x, 1 + y, 4, 2)
        f(1 + x, 3 + y, 4, 2)
        f(1 + x, 5 + y, 4, 2)
        f(1 + x, 1 + y, 2, 6)
        f(3 + x, 3 + y, 2, 4)
    elif(rank == 7):
        positions = [[8, 5], [14, 5], [8, 17], [14, 17], [11, 11], [8, 31], [14, 31]]
        flip_range = 4

        f(1 + x, 1 + y, 4, 2)
        f(3 + x, 1 + y, 2, 6)
    elif(rank == 8):
        positions = [[8, 5], [14, 5], [8, 17], [14, 17], [11, 11], [8, 31], [14, 31], [11, 25]]
        flip_range = 4

        f(1 + x, 1 + y, 4, 2)
        f(1 + x, 3 + y, 4, 2)
        f(1 + x, 5 + y, 4, 2)
        f(3 + x, 1 + y, 2, 6)
        f(1 + x, 1 + y, 2, 6)
    elif(rank == 9):
        positions = [[8, 5], [11, 10], [8, 15], [14, 15], [14, 5], [8, 31], [14, 31], [8, 21], [14, 21]]
        flip_range = 4

        f(1 + x, 1 + y, 4, 2)
        f(1 + x, 3 + y, 4, 2)
        f(3 + x, 1 + y, 2, 6)
        f(1 + x, 1 + y, 2, 4)
    elif(rank == 10):
        positions = [[8, 5], [11, 10], [8, 15], [14, 15], [14, 5], [8, 31], [14, 31], [8, 21], [14, 21], [11, 26]]
        flip_range = 4
        
        f(1 + x, 1 + y, 2, 6)
        f(3 + x, 1 + y, 4, 2)
        f(3 + x, 5 + y, 4, 2)
        f(5 + x, 1 + y, 2, 6)
        f(3 + x, 1 + y, 2, 6)
    elif(rank == 11):#jack
        #crown
        f(7 + x, 8 + y, 10, 4)
        f(7 + x, 7 + y, 2, 2)
        f(9 + x, 7 + y, 2, 2)
        f(11 + x, 7 + y, 2, 2)
        f(13 + x, 7 + y, 2, 2)
        f(15 + x, 7 + y, 2, 2)

        f(1 + x, 1 + y, 4, 2)
        f(2 + x, 1 + y, 2, 6)
        f(1 + x, 5 + y, 3, 2)

        f(8 + x, 12 + y, 8, 3)
        f(11 + x, 14 + y, 3, 12)
        f(8 + x, 24 + y, 5, 3)
    elif(rank == 12):#queen
        #crown
        f(7 + x, 8 + y, 10, 4)
        f(7 + x, 7 + y, 2, 2)
        f(9 + x, 7 + y, 2, 2)
        f(11 + x, 7 + y, 2, 2)
        f(13 + x, 7 + y, 2, 2)
        f(15 + x, 7 + y, 2, 2)

        f(1 + x, 1 + y, 4, 2)
        f(1 + x, 1 + y, 2, 5)
        f(3 + x, 1 + y, 2, 4)
        f(1 + x, 4 + y, 3, 2)
        f(3 + x, 5 + y, 2, 2)

        f(8 + x, 12 + y, 8, 3)
        f(8 + x, 12 + y, 3, 15)
        f(13 + x, 12 + y, 3, 12)
        f(8 + x, 24 + y, 5, 3)
        f(11 + x, 22 + y, 4, 4)
        f(13 + x, 24 + y, 3, 3)
    elif(rank == 13):#king
        #crown
        f(7 + x, 8 + y, 10, 4)
        f(7 + x, 7 + y, 2, 2)
        f(9 + x, 7 + y, 2, 2)
        f(11 + x, 7 + y, 2, 2)
        f(13 + x, 7 + y, 2, 2)
        f(15 + x, 7 + y, 2, 2)
        
        f(1 + x, 1 + y, 2, 6)
        f(3 + x, 1 + y, 2, 3)
        f(3 + x, 4 + y, 2, 3)
        f(1 + x, 3 + y, 3, 2)
        
        f(8 + x, 12 + y, 3, 15)
        f(13 + x, 12 + y, 3, 7)
        f(13 + x, 20 + y, 3, 7)
        f(8 + x, 18 + y, 7, 3)
    elif(rank == 1):#ace
        f(1 + x, 1 + y, 2, 6)
        f(3 + x, 1 + y, 2, 6)
        f(1 + x, 1 + y, 4, 2)
        f(1 + x, 3 + y, 4, 2)

        if(suit == 0):
            f(4 + x, 19 + y, 16, 4)
            f(5 + x, 18 + y, 5, 6)
            f(14 + x, 18 + y, 5, 6)
            f(5 + x, 18 + y, 14, 2)
            f(6 + x, 17 + y, 12, 2)
            f(7 + x, 16 + y, 10, 2)
            f(8 + x, 15 + y, 8, 2)
            f(9 + x, 14 + y, 6, 2)
            f(10 + x, 12 + y, 4, 3)
            f(11 + x, 10 + y, 2, 17)
            f(10 + x, 25 + y, 4, 2)
        elif(suit == 1):
            f(11 + x, 18 + y, 2, 9)
            f(9 + x, 25 + y, 6, 2)
            d.fill_circle(8 + x, 20 + y, 4)
            d.fill_circle(16 + x, 20 + y, 4)
            d.fill_circle(12 + x, 15 + y, 4)

            s_co(255, 255, 255)
            f(8 + x, 16 + y, 2, 2)
            f(9 + x, 17 + y, 2, 2)
            f(14 + x, 16 + y, 2, 2)
            f(13 + x, 17 + y, 2, 2)
        elif(suit == 2):
            f(11 + x, 25 + y, 2, 2)
            f(10 + x, 24 + y, 4, 2)
            f(9 + x, 23 + y, 6, 2)
            f(8 + x, 22 + y, 8, 2)
            f(7 + x, 21 + y, 10, 2)
            f(6 + x, 20 + y, 12, 2)
            f(5 + x, 19 + y, 14, 2)
            f(4 + x, 13 + y, 16, 7)
            f(4 + x, 12 + y, 8, 2)
            f(5 + x, 11 + y, 6, 2)
            f(6 + x, 10 + y, 4, 2)
            f(12 + x, 12 + y, 8, 2)
            f(13 + x, 11 + y, 6, 2)
            f(14 + x, 10 + y, 4, 2)
        elif(suit == 3):
            f(11 + x, 8 + y, 2, 23)
            f(10 + x, 10 + y, 2, 19)
            f(9 + x, 12 + y, 2, 15)
            f(8 + x, 14 + y, 2, 11)
            f(7 + x, 16 + y, 2, 7)
            f(6 + x, 18 + y, 2, 3)
            f(12 + x, 10 + y, 2, 19)
            f(13 + x, 12 + y, 2, 15)
            f(14 + x, 14 + y, 2, 11)
            f(15 + x, 16 + y, 2, 7)
            f(16 + x, 18 + y, 2, 3)

    
    if(rank > 1 and rank < 11):
        i = 0
        for pos in positions:
            if(suit == 0 or suit == 1):#spades or clubs
                dr_spadeclub(pos[0] + x, pos[1] + y, i > flip_range)
                i += 1
            elif(suit == 2):
                dr_heart(pos[0] + x, pos[1] + y, i > flip_range)
                i += 1
            elif(suit == 3):
                dr_diamond(pos[0] + x, pos[1] + y)
                i += 1

def dr_hand():
    for i in range(len(c_ha)):
        cur_card = c_ha[i]
        dr_card(cur_card[0], cur_card[1], 86 + (i * 26), 145)

def detect_hand_type():
    global n_c
    global su_c
    global c_ha
    global st
    global f_h
    global h_r_c
    global h_r
    global fl
    global pair_ranks

    n_c = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    su_c = [0, 0, 0, 0]

    st = False
    for i in range(len(c_ha)):
        if(s_c[i]):
            card = c_ha[i]
            su_c[card[0]] += 1
            n_c[card[1] - 1] += 1

    h_r_c = max(n_c)
    h_r = 2
    for i in range(len(n_c)):
        if(n_c[i] == h_r_c and ((i + 1) > h_r or i == 0)):
            h_r = i + 1

        
    f_h = (3 in n_c and 2 in n_c)
    fl = 5 in su_c

    for i in range(10):
        if(i < 9):
            if(n_c[i] == 1 and n_c[i + 1] == 1 and n_c[i + 2] == 1 and n_c[i + 3] == 1 and n_c[i + 4] == 1):
                st = True
        elif(n_c[9] == 1 and n_c[10] == 1 and n_c[11] == 1 and n_c[12] == 1 and n_c[1] == 1):
            st = True

    pair_ranks = []
    for i in range(len(n_c)):
        num = n_c[i]
        if(num == 2):
            pair_ranks.append(i + 1)

    if(st and fl):
        up_hand_type(1)
    elif(h_r_c == 4):
        up_hand_type(2)
    elif(f_h):
        up_hand_type(3)
    elif(fl):
        up_hand_type(4)
    elif(st):
        up_hand_type(5)
    elif(h_r_c == 3):
        up_hand_type(6)
    elif(len(pair_ranks) == 2):
        up_hand_type(7)
    elif(h_r_c == 2):
        up_hand_type(8)
    elif(h_r_c == 1):
        up_hand_type(9)
    else:
        up_hand_type(0)      

def level_hand():
    global c_ha_t
    lc, lm = hand_levels[c_ha_t]
    n, oc, om = hand_types[c_ha_t]
    hand_types[c_ha_t] = (n, oc + lc, om + lm)

def select_card(index):
    global s_c_c
    if(not s_c[index]):
        if(s_c_c < 5):
            s_c[index] = True
            up_card_select_redical(index)
            s_c_c += 1
    else:
        s_c[index] = False
        up_card_select_redical(index)
        s_c_c -= 1
    detect_hand_type()

def delete():
    if(c_m == "shop" or c_m == "blind"):
        if(c_s_j is not None):
            if(c_ho[1] == 0 and c_ho[0] < len(c_js)):
                sell_joker()

def generate_hand():
    for i in range((ha_s if len(c_d) >= ha_s else len(c_d)) - len(c_ha)):
        index = rr(0, len(c_d))
        c_ha.append(c_d[index])
        c_d.pop(index)
    dr_hand()

def cl_s_c():
    global s_c_c
    sel = 0
    for i in range(8):
        if(s_c[i]):
            c_ha.pop(i - sel)
            sel += 1
            s_c[i] = False
            up_card_select_redical(i)
    s_c_c = 0
    up_hand_type(0)

def c_of_card(rank):
    return 11 if rank == 1 else 10 if rank > 9 else rank

def scoring_cards():
    for i in range(len(c_ha)):
        score_card(i)
def score_card(i, rt = False):
    global mo
    if(s_c[i]):
        card = c_ha[i]
        if(fl or st or f_h or card[1] == h_r or card[1] in pair_ranks):
            up_c(c + c_of_card(card[1]))
            for jkr in c_js:
                if("Wrathful" in jkr and card[0] == 0):
                    up_m(m + 3)
                elif("Gluttonous" in jkr and card[0] == 1):
                    up_m(m + 3)
                elif("Lusty" in jkr and card[0] == 2):
                    up_m(m + 3)
                elif("Greedy" in jkr and card[0] == 3):
                    up_m(m + 3)
                elif("Even" in jkr and card[1] % 2 == 0 and card[1] < 11):
                    up_m(m + 4)
                elif("Odd" in jkr and card[1] % 2 == 1 and card[1] < 11):
                    up_m(m + 4)
                elif("Chad" in jkr and i == s_c.index(True) and not rt):
                    for j in range(2):
                        score_card(i, True)
                elif("Photo" in jkr):
                    f_cas = [c for c in c_ha if c[1] >= 11 and c[1] <= 13 and s_c[c_ha.index(c)]]
                    if(len(f_cas) < 1):
                        continue
                    if(i == c_ha.index(f_cas[0])):
                        up_m(m * 2)
                elif("Selt" in jkr and se_rt > 0 and not rt):
                    score_card(i, True)
                elif("Gem" in jkr and card[0] == 3):
                    mo += 1
                elif("Blood" in jkr and card[0] == 2):
                    up_m(round(m * (1.5 if rr(0, 2) == 0 else 1)))
                elif("Onyx" in jkr and card[0] == 1):
                    up_m(m + 7)
                elif("Arrow" in jkr and card[0] == 0):
                    up_c(c + 50)

def after_scoring():
    global r_m
    for j in c_js:
        if("Jimbo" in j):
            up_m(m + 4)
        elif("Swash" in j):
            for jkr in c_js:
                if(jkr is not j):
                    if("Blueprint" in jkr):
                        up_m(m + j_info.get("Blueprint")[2])
                    else:
                        up_m(m + j_info.get(jkr)[2])
        elif("Misprint" in j):
            up_m(m + rr(0, 24))
        elif("Half" in j):
            if(s_c_c <= 3):
                up_m(m + 20)
        elif("Space" in j and rr(0, 4) == 0):
            level_hand()
        elif("Sharp" in j and c_ha_t in played_types):
            up_m(m * 3)
        elif("Boot" in j):
            up_m(m + round(mo * 2 / 5))
        elif("Bull" in j):
            up_c(c + (mo * 2))
        elif("Ramen" in j and r_m > 1):
            up_m(m * r_m)
        elif("Stunt" in j):
            up_c(c + 250)

def calc_score():
    up_sc(sc + (c * m))

def finish_round():
    global c_d
    global played_types
    dr_shop_screen()

    blind = c_r % 3
    up_mo(mo + (h) + (3 if blind == 1 else 4 if blind == 2 else 5))
    up_c_r(c_r + 1)

    se_sub = False

    for jkr in c_js:
        if("Golden" in jkr):
            up_mo(mo + 4)
        if("Rocket" in jkr):
            up_mo(mo + 1 + ((a - 1) * 2))
        if("Selt" in jkr and not se_sub):
            global se_rt
            se_rt -= 1
    up_h(t_h)
    up_di(t_d)

    if(blind == 0):
        up_a(a + 1)
        if(a == 9):
            playing = False
            print("You win!")
    c_d = t_de.copy()
    played_types = []
    
def play_hand():
    up_h(h - 1)

    scoring_cards()
    after_scoring()
    calc_score()

    played_types.append(c_ha_t)

    cl_s_c()
    if(sc >= n_sc):
        finish_round()
        return   
    generate_hand()

def discard():
    global mo
    global s_c_c
    global t_d
    for jkr in c_js:
        if("Faceless" in jkr):
            amt = 0
            for i in range(8):
                if(s_c[i]):
                    if(c_ha[i][0] >= 11 or c_ha[i][0] <= 13):
                        amt += 1
            if(amt >= 3):
                mo += 5
        elif("Ramen" in jkr):
            global r_m
            r_m -= s_c_c * .01
        elif("Burnt" in jkr):
            if(di == t_d):
                level_hand()

    up_di(di - 1)
    cl_s_c()
    generate_hand()

def set_move_redical():
    global c_m_j
    global c_s_j
    global c_m_j_index
    global c_ho
    c_m_j = c_s_j
    c_m_j_index = c_ho[0]
    
    x, y = hover_pos[c_m][0][c_m_j_index]
    x -= 2
    y -= 2

    dr_move_redical(x + 1, y + 1)

def dr_move_redical(x, y):
    s_co(255, 255, 255)
    f(-1 + x, -1 + y, 12, 2)
    f(0 + x, 0 + y, 10, 2)
    f(1 + x, 1 + y, 8, 2)
    f(2 + x, 2 + y, 6, 2)
    f(3 + x, 3 + y, 4, 2)
    f(4 + x, 4 + y, 2, 2)

def cl_move_redical():
    global c_m_j
    x, y = hover_pos[c_m][0][c_m_j_index]
    x -= 2
    y -= 2

    s_co(59,117,93)
    f(x, y, 12, 7)
    c_m_j = None

def move_joker():
    global c_s_j
    global c_m_j_index
    global c_m_j
    global c_js

    cl_move_redical()

    old = c_s_j
    c_js[c_ho[0]] = c_m_j
    c_js[c_m_j_index] = old

    for jkr in c_js:
        if("Blueprint" in jkr):
            check_bp(c_js.index(jkr))

    cl_joker_description()
    c_m_j = None

    dr_held_jokers()

def generate_shop():
    global c_h_js
    global c_js
    c_h_js = []
    i = 0
    while i < 3:
        v = rr(1, 101)
        l = [j for j,val in j_info.items() if val[3] == (0 if v >= 31 else 1 if v >= 6 else 2)]
        if(not l):
            continue
        js = c_js.copy()
        l = [j for j in l if j not in c_js and j not in c_h_js]
        for jkr in js:
            if("Blueprint" in jkr and "Blueprint" in l):
                l.remove("Blueprint")
        if(not l):
            continue
        c_h_js.append(l[rr(len(l))]) 
        i += 1  
    dr_shop_jokers()

def reroll():
    global r_c
    global mo
    if(mo >= r_c):
        up_mo(mo - r_c)
        r_c += 1
        generate_shop()

def select():
    global c_s_j
    global c_m_j
    global ch_j_s
    global c_m_j_index

    if(c_m == "shop"):
        if(c_s_j is None):
            if(c_ho[1] == 0 and c_ho[0] < len(c_js)):
                c_s_j = c_js[c_ho[0]]
            elif(c_ho[1] == 1):
                if(c_ho[0] > 0 and c_ho[0] - 1 < len(c_h_js)):
                    c_s_j = c_h_js[c_ho[0] - 1]
                elif(c_ho[0] == 0):
                    dr_blind_screen()
            elif(c_ho[1] == 2):
                reroll()
            if(c_s_j is not None):
                if(c_m_j is not None and c_m_j != c_s_j):
                    move_joker()
                elif(c_m_j == c_s_j):
                    c_m_j = None
                else:
                    jkr_desc_sel(c_s_j)
        else:
            if(c_ho[1] == 1):
                buy_joker()
            elif(c_ho[1] == 0):
                set_move_redical()
    elif(c_m == "blind"):
        if(c_s_j is None):
            if(c_ho[1] == 0 and c_ho[0] < len(c_js)):
                c_s_j = c_js[c_ho[0]]
            if(c_s_j is not None):
                if(c_m_j is not None and c_m_j != c_s_j):
                    move_joker()
                elif(c_m_j == c_s_j):
                    c_m_j = None
                else:
                    jkr_desc_sel(c_s_j)
        else:
            if(c_ho[1] == 0):
                set_move_redical()
        if(c_ho[1] == 1):
            select_card(c_ho[0])
        elif(c_ho[1] == 2):
            if(c_ho[0] == 0 and h > 0):
                play_hand()
            elif(c_ho[0] == 1 and di > 0):
                discard()

def set_menu(name):
    global c_m
    global c_ho
    c_m = name
    c_ho = [0, 0]

def dr_shop_screen():
    set_menu("shop")
    cl_panel()
    dr_background()
    dr_shop_panel()
    generate_shop()
    up_mo(mo)
    up_hover_redical()  

def dr_blind_screen():
    global r_c
    r_c = 5
    cl_panel()
    dr_background()
    dr_blind_panel()
    cl_joker_description()

    s_co(0, 147, 253)
    f(142, 195, 46, 12)
    
    s_co(255, 73, 64)
    f(190, 195, 46, 12)

    s_co(255, 255, 255)
    w_t("PLAY", 154, 198)
    w_t("DISCARD", 193, 198)

    set_menu("blind")
    generate_hand()
    up_sc(0)

dr_banner()
up_a(1)
up_c_r(1)
up_di(t_d)
up_h(t_h)
up_c(0)
up_m(0)
up_sc(0)
dr_held_jokers()
dr_blind_screen()
playing = True
while playing:
    key = s.wait_key()

    #directional keys
    if((key >= 24 and key <= 26) or key == 34):
        change_hover(key)
        up_hover_redical()
    elif(key == 105):#enter key
        select()
    elif(key == 23):
        delete()
    if(key == 45 or (h == 0 and sc < n_sc)):
        playing = False
del letters
del c_js
del c_h_js
del sprs
del j_sprs
del j_info
del palletes
del jimbo_vars
del hand_levels
del hand_types
del blind_panels