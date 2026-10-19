import math
#path = input("Path: ").replace("\\", "/").replace("\"", "")
path = "C:\\Users\\chris\\Documents\\Projects\\TI-Projects\\Resvecgr\\1.2\\RESGREVO.py"
funcs = []
vars = []
out = ""

def get_letter(num):
    match num:
        case 0:
            return ""
        case 1:
            return "A"
        case 2:
            return "B"
        case 3:
            return "C"
        case 4:
            return "D"
        case 5:
            return "E"
        case 6:
            return "F"
        case 7:
            return "G"
        case 8:
            return "H"
        case 9:
            return "I"
        case 10:
            return "J"
        case 11:
            return "K"
        case 12:
            return "L"
        case 13:
            return "M"
        case 14:
            return "N"
        case 15:
            return "O"
        case 16:
            return "P"
        case 17:
            return "Q"
        case 18:
            return "R"
        case 19:
            return "S"
        case 20:
            return "T"
        case 21:
            return "U"
        case 22:
            return "V"
        case 23:
            return "W"
        case 24:
            return "X"
        case 25:
            return "Y"
        case 26:
            return "Z"

num = 1
def get_name():
    global num
    l_1 = math.floor((num - 1) / 26)
    l_2 = num - l_1 * 26

    num += 1
    return get_letter(l_1) + get_letter(l_2)


with open(path, "r") as file:
    for line in file.readlines():
        if("def " in line and ":" in line.strip()[len(line.strip()) - 1:]):
            begin_vars_ind = line.strip().index("(")
            funcs.append([line.strip()[4:begin_vars_ind], get_name()])
            vars_list = line.strip()[begin_vars_ind + 1:line.strip().index(")")].split(",")
            for var in vars_list:
                vars.append([var.strip(), get_name()])

        if(" = " in line and not ")" in line.strip()[len(line.strip()) - 1:]):
            already_exists = False
            for var in vars:
                if(var[0] in line.split(" = ")[0]):
                    already_exists = True
                    break
            if(not already_exists):
                vars.append([line.split(" = ")[0].strip(), get_name()])

        for func in funcs:
            if(func[0] + "(" in line):
                line = line.replace(func[0] + "(", func[1] + "(")
        
        for var in vars:
            print(var)
            before_after = line.split(var[0])
            new_line = before_after[0]
            for i in range(len(before_after) - 1):
                before = before_after[i].strip()
                after = before_after[i + 1].strip()

                if(not before[len(before) - 1:].isalnum() and not after[:1].isalnum()):
                    new_line += var[1] + after
                else:
                    new_line += var[0] + after
            #if(var[0] in line and not var[0] + "(" in line):
            #    line = line.replace(var[0], var[1])

        for i in range(len(line)):
            if(not line[i:i + 1].isspace()):
                out += line.rstrip() + "\n"
                break
print(vars)


split_by_slash = path.split("/")
with open(split_by_slash[len(split_by_slash) - 1], "w") as file:
    file.write(out)