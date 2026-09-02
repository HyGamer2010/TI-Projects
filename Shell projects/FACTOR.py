def synthetic(i):
    global coeffs
    global rootsLeft
    ncoeffs = coeffs.copy()
    for j in range(len(ncoeffs) - 2):
        ncoeffs[j + 1] += (i * ncoeffs[j])
    ncoeffs[len(ncoeffs) - 1] += (ncoeffs[len(ncoeffs) - 2] * i)
    if(ncoeffs[len(ncoeffs) - 1] == 0):
        ncoeffs.pop()
        rootsLeft -= 1
        roots.append(i)
        coeffs = ncoeffs
        return True
    return False

def parse_roots():
    out = ""
    for root in roots:
        out += "(x" + ("+" if root < 0 else "-") + str(abs(root)) + ")"
    return out

def parse_coefficents():
    if(len(coeffs) == 1):
        return ""
    else:
        out = "(" + (str(coeffs[0]) if coeffs[0] > 1 else "") + ("x^" if rootsLeft > 1 else "x" if rootsLeft > 0 else "") + (str(rootsLeft) if rootsLeft > 1 else "")
        for i in range(len(coeffs) - 1):
            i += 1
            cur_coeff = coeffs[i]
            if(cur_coeff == 0):
                continue
            exp = rootsLeft - i
            out += ("+" if cur_coeff >= 0 else "-") + (str(abs(cur_coeff)) if abs(cur_coeff) > 1 else "") + ("x^" if exp > 1 else "x" if exp > 0 else "") + (str(exp) if exp > 1 else "")
        return out + ")"
while(True):
    coeffs = []
    roots = []
    degree = int(input("Degree: "))
    for i in range(degree + 1):
        coeffs.append(int(input(("Coefficient " + str(i + 1) + ":") if i < degree else "Constant: ")))

    rootsLeft = degree
    while rootsLeft > 0:
        first = abs(coeffs[0])
        final = abs(coeffs[len(coeffs) - 1])
        root_count = len(roots)
        for i in range(2 * final + 1):
            to_break = False
            i -= final
            if(i == 0):
                to_break = synthetic(i)
            elif(final % i == 0):
                to_break = synthetic(i)
            if(to_break):
                break
        if(len(roots) == root_count):
            break

    print(parse_roots() + parse_coefficents())
    print("----------")