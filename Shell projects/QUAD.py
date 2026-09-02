import math

def check_prime(num):
    for i in range(num - 3):
        i += 2
        if(num % i == 0):
            return False
    return True

def simplify_radical(radicand):
    if(int(math.sqrt(radicand)) == math.sqrt(radicand)):
        return [int(math.sqrt(radicand)), 1]
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
        return([coefficient, final_radicand])
    else:
        return (1, radicand)

def m_gcd(*nums):
    new_nums = []
    for i in range(len(nums)):
        new_nums.append(abs(nums[i]))
    gcd = 1
    for i in range(max(*new_nums)):
        i += 1
        is_d = True
        for num in new_nums:
            if(num % i != 0):
                is_d = False
        if(is_d):
            gcd = i
    return gcd
        
while True:
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))

    discriminant = b**2 - (4 * a * c)
    is_complex = False
    if(discriminant < 0):
        is_complex = True
        discriminant = -discriminant
    radical = simplify_radical(discriminant)
    divisor = 2 * a

    if(is_complex or radical[1] != 1):
        gcd = m_gcd(radical[0], b, divisor)

        if(gcd != 1):
            radical[0] /= gcd
            b /= gcd
            divisor /= gcd
        print("(" + (str(-b) + "+" if b != 0 else "") + ("(" if radical[1] > 1 else "") + (str(radical[0]) + "*" if radical[0] != 1 else "") + ("i" if is_complex else "") + ("*sqrt(" + str(radical[1]) + ")" if radical[1] > 1 else "") + ")" + ("/" + str(divisor) if divisor > 1 else "") + ",(" + (str(-b) + "-" if b != 0 else "") + ("(" if radical[1] > 1 else "") + (str(radical[0]) + "*" if radical[0] != 1 else "") + ("i" if is_complex else "") + ("*sqrt(" + str(radical[1]) + ")" if radical[1] > 1 else "") + ")" + ("/" + str(divisor) if divisor > 1 else ""))
    else:
        pos_div = divisor
        pos_num = -b + radical[0]
        pos_gcd = m_gcd(pos_div, pos_num)
        if(pos_gcd != 1):
            pos_num /= pos_gcd
            pos_div /= pos_gcd
        neg_div = divisor
        neg_num = -b - radical[0]
        neg_gcd = m_gcd(neg_div, neg_num)
        if(neg_gcd != 1):
            neg_num /= neg_gcd
            neg_div /= neg_gcd
        print(str(pos_num) + ("/" + str(pos_div) if pos_div > 1 else "") + "," + str(neg_num) + ("/" + str(neg_div) if neg_div > 1 else ""))
    print("---------")
