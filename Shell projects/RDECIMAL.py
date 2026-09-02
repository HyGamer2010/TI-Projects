import math
num = int(input("Numerator: "))
den = int(input("Denominator: "))

out = str(math.floor(num/den)) + "."
cut_out = len(out)
i = cut_out

cur_num = num * (10**(cut_out - 1))
dec_started = False
while out[cut_out:i] not in out[i:] or len(out) < cut_out or out[cut_out:i] == "":
    i += 1
    for j in range(2):
        if(cur_num / den >= 1):
            out += str(math.floor(cur_num / den))
            cur_num -= math.floor(cur_num / den) * den
            dec_started = True
        elif(not dec_started):
            cut_out += 1
            out += "0"
        else:
            out += "0"
        cur_num *= 10
print(out[:i])