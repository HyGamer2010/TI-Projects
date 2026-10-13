import ti_system
import math
while(True):
    first_vec = True
    last_vec = False
    components = [0, 0]
    while(not last_vec):
        magnitude = float(input("What is the length of the vector?\n"))
        on_axis = input("Does your angle lie on an axis?\n1: Yes\n2: No\n") == "1"
        if(on_axis):
            direction = input("What axis does it lie on?\n1. North\n2. East\n3. South\n4. West\n")
            if(direction == "1"):
                components[1] += magnitude
            elif(direction == "2"):
                components[0] += magnitude
            elif(direction == "3"):
                components[1] -= magnitude
            elif(direction == "4"):
                components[0] -= magnitude
        else:
            angle = input("Fill in the blank: ____ degrees _____ of _____\nWhat is the angle?\n")
            direction = int(input("Fill in the blank: " + angle + " degrees _____ of _____\nWhat is the direction?\n1. North\n2. East\n3. South\n4. West\n"))
            if(direction == 1):
                dirname = "North"
            elif(direction == 2):
                dirname = "East"
            elif(direction == 3):
                dirname = "South"
            elif(direction == 4):
                dirname = "West"
            
            axis = int(input("Fill in the blank: " + angle + " degrees " + dirname + " of _____\nWhat is the base axis?\n1. North\n2. East\n3. South\n4. West\n"))
            angle = float(angle)

            if(axis == 1 or axis == 3):
                angle = 90.0 - angle

            angle = math.radians(angle)

            xcomp = magnitude * math.cos(angle)
            ycomp = magnitude * math.sin(angle)

            if(axis == 4 or direction == 4):
                xcomp = -xcomp
            if(axis == 3 or direction == 3):
                ycomp = -ycomp
            components[0] += xcomp
            components[1] += ycomp
        
        if(first_vec):
            first_vec = False
        else:
            last_vec = input("Is that the last vector?\n1. Yes\n2. No\n") == "1"

    res_magnitude = round((components[0]**2 + components[1]**2)**(.5), 1)

    if(components[0] != 0):
        reference_angle = math.atan(abs(components[1]/components[0]))
        deg_angle = round(math.degrees(reference_angle), 1)

        directions = ["East" if components[0] > 0 else "West", "North" if components[1] > 0 else "South"]
        print(str(res_magnitude) + " units " + str(deg_angle) + " degrees " + directions[1] + " of " + directions[0] + "\nor\n" + str(res_magnitude) + " units " + str(round(90 - deg_angle, 1)) + " degrees " + directions[0] + " of " + directions[1])
    else:
        direction = "North" if components[1] > 0 else "East" if components[0] > 0 else "South" if components[1] < 0 else "West"
        print(str(res_magnitude) + " units " + direction)

    ti_system.wait_key()
    print("\n\n\n\n")