equ = input("Enter equation:\n")

terms : str = []
current_term = "+" if equ[:1] != "-" else ""

for c in equ:
    if((c == "+" or c == "-") and len(current_term) > 0):
        terms.append(current_term)
        current_term = c
    else:
        current_term += c
terms.append(current_term)

for term in terms:
    term = term.replace("sqrt(X)", "X**(1/2)*")
    term = term.replace('**', '^')
    if("X" in term):
        term = term.replace("X", "*X")
        for i in range(len(term)):
            if(i == 0 and term[i:i + 1] == "*"):
                term = "1" + term
            elif(not term[i - 1:i].isdigit() and term[i:i + 1] == "*"):
                term = term[:i] + "1" + term[i:]
    num = ""
    denom = ""
    in_num = True

    current_number = ""
    for i in range(len(term)):
        c = term[i:i + 1]
        if(c == "*" or i == len(term) - 1):
            if("^" in current_number):
                exponent = eval(current_number.split("^")[1])
                final = str(exponent) + "*X" + str(exponent - 1)
            else:
                final = current_number
            if(in_num):
                num += final
            else:
                denom += final
        else:
            current_number += c
print(num)