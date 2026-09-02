import math

def check_prime(num):
    for i in range(num - 3):
        i += 2
        if(num % i == 0):
            return False
    return True

while True:
    radicand = int(input("Radicand: "))
    if(int(math.sqrt(radicand)) == math.sqrt(radicand)):
        print(math.sqrt(radicand))
    elif(not check_prime(radicand)):
        factors = [radicand]
        final_factors = []
        while len(factors) > 0:
            for factor in factors:
                for i in range(factor - 3):
                    i += 2
                    if(factor % i == 0):
                        factors.remove(factor)
                        new_fac = int(factor / i)
                        if(check_prime(new_fac)):
                            final_factors.append(new_fac)
                        else:
                            factors.append(new_fac)
                        if(check_prime(i)):
                            final_factors.append(i)
                        else:
                            factors.append(i)
                        break
        pairs = []
        for i in range(len(final_factors)):
            if(i > len(final_factors) - 1):
                break
            factor = final_factors[i]
            for j in range(len(final_factors)):
                if(final_factors[j] == factor and i != j):
                    pairs.append(final_factors[j])
                    if(i > j):
                        final_factors.pop(i)
                        final_factors.pop(j)
                    else:
                        final_factors.pop(j)
                        final_factors.pop(i)
                    break
        coefficient = 1
        final_radicand = 1
        for i in pairs:
            coefficient *= i
        for i in final_factors:
            final_radicand *= i
        print((str(coefficient) + "*" if coefficient > 1 else "") + "sqrt(" + str(final_radicand) + ")")
    else:
        print("sqrt(" + str(radicand) + ")")
    print("---------")