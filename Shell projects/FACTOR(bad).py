import math

root3 = None

def simplify_fraction(num, den):
    gcd = math.gcd(num, den)
    return (str(int(num / gcd)), str(int(den / gcd)))

def quadratic_formula(a, b, c):
    x1 = (-b + math.sqrt(b * b - (4 * a * c)))
    x2 = (-b - math.sqrt(b * b - (4 * a * c)))
    x1div = x1 / (2 * a)
    x2div = x2 / (2 * a)
    coeff1 = None
    coeff2 = None
    if(round(x1div) != x1div or round(x2div) != x2div):
        if(input("At least 1 of your answers come out as a decimal. Would you like you answers to be fractions? (y/n)") == "y"):
            if(round(x1div) != x1div):
                mult = int(10 ** len(str(x1)[2:]))
                frac = simplify_fraction(int(x1 * mult), int((2 * a) * mult))
                x1 = frac[0]
                coeff1 = frac[1]
            else:
                x1 = int(abs(x1div))
            if(round(x2div) != x2div):
                mult = int(10 ** len(str(x2)[2:]))
                frac = simplify_fraction(int(x2 * mult), int((2 * a) * mult))
                x2 = frac[0]
                coeff2 = frac[1]
            else:
                x2 = int(abs(x2div))
    else:
        x1 = int(abs(x1div))
        x2 = int(abs(x2div))
    return x1, x2, coeff1, coeff2, x1div, x2div

if(input("Degree 2 or degree 3 polynomial?") == "2"):
    print("Format: ax^2 + bx + c = 0")
    a = float(input("a:"))
    b = float(input("b:"))
    c = float(input("c:"))

    vals = quadratic_formula(a, b, c)

    print("(" + (str(vals[2]) if vals[2] is not None else "") + "x " + ("+" if vals[4] <= 0 else "-") + " " + str(vals[0]) + ")" + " (" + (str(vals[3]) if vals[3] is not None else "") + "x " + ("+" if vals[5] <= 0 else "-") + " " + str(vals[1]) + ")")
else:
    print("Format: ax^3 + bx^2 + cx + d = 0")
    a = int(float(input("a:")))
    b = float(input("b:"))
    c = float(input("c:"))
    d = int(float(input("d:")))

    for i in range((a if a < d else d)):
        i += 1
        if(a % i == 0 and d % i == 0):
            root3 = i
            nb = (a * i) + b
            nc = (a * (i**2)) + (b * i) + c
            break
    print(a, nb, nc)
    vals = quadratic_formula(a, nb, nc)
    print("(x "+ ("+" if root3 <= 0 else "-") + " " + str(int(root3)) + ") (" + (str(vals[2]) if vals[2] is not None else "") + "x " + ("+" if vals[4] <= 0 else "-") + " " + str(vals[0]) + ")" + " (" + (str(vals[3]) if vals[3] is not None else "") + "x " + ("+" if vals[5] <= 0 else "-") + " " + str(vals[1]) + ")")
