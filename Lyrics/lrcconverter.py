#https://subtitletools.com/timed-lyrics-editor

import pylrc

with open("Story of a Warrior.lrc", "r", encoding="UTF-8") as file:
    lrc = file.read()

subs = pylrc.parse(lrc)

with open("out.txt", "w") as file:
    for sub in subs:
        file.write(f"[{sub.time},\"{sub.text.strip().upper()}\"],\n")