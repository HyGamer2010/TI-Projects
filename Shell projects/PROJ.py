import math
s = float(input("Distance(m): "))
t = float(input("Time(s): "))
d = s / t #Horizontal velocity
e = 9.8 * (.5 * t) #Vertical velocity gained from gravity over time assuming projectile launches and lands at the same spot
c = 4.9 * ((.5 * t)**2) #Maximum vertical height reached
v = math.sqrt((d**2) + (e**2)) #Initial velocity using pythagorean theorem
a = math.atan(e/d) #Angle in rad
print("Initial Vertical velocity: " + str(e))
print("Horizontal Velocity: " + str(d))
print("Max delta Y: " + str(c))
print("Initial Velocity: " + str(v))
print("Angle: " + str(a))