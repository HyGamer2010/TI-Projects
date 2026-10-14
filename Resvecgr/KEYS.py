import ti_system

CLEAR = 45

ti_system.disp_clr()
ti_system.disp_at(1, "Press keys!", "center")
ti_system.disp_at(2, "CLEAR to quit", "center")

while True:
    # 0 = poll without waiting
    k = ti_system.get_key(0)
    if k == CLEAR:
        break
    if k != 0:
        ti_system.disp_at(5, "Key code: " + str(k), "center")