import math

def simplify(frac):
    numerator, denominator = frac

    if numerator == 0: 
        return [0, 1]
    
    if denominator < 0:
        numerator = numerator * -1
        denominator = abs(denominator)

    common_divisor = math.gcd(numerator, denominator)
    simplified_numerator = numerator // common_divisor
    simplified_denominator = denominator // common_divisor

    return [simplified_numerator, simplified_denominator]

def check_errors(frac):
    if not isinstance(frac, (list, tuple)):
        raise ValueError("Ulamek nie jest poprawny!")
    if len(frac)!=2:
        raise ValueError("Ulamek powienien skladac sie z wylacznie 2 liczb!")
    for number in frac:
        if not isinstance(number, int):
            raise ValueError("Ulamek zawiera liczby zmiennoprzecinkowe!")
    if frac[1] == 0:
        raise ValueError("Ulamek ma w mianowniku zero!")

def add_frac(frac1, frac2):        # frac1 + frac2
    check_errors(frac1)
    check_errors(frac2)

    result = []
    result.append(frac1[0]*frac2[1]+frac2[0]*frac1[1])
    result.append(frac1[1]*frac2[1])
    return simplify(result)

def sub_frac(frac1, frac2):        # frac1 - frac2
    check_errors(frac1)
    check_errors(frac2)

    result = []
    result.append(frac1[0]*frac2[1]-frac2[0]*frac1[1])
    result.append(frac1[1]*frac2[1])
    return simplify(result)

def mul_frac(frac1, frac2):         # frac1 * frac2
    check_errors(frac1)
    check_errors(frac2)

    result = []
    result.append(frac1[0]*frac2[0])
    result.append(frac1[1]*frac2[1])
    return simplify(result)

def div_frac(frac1, frac2):         # frac1 / frac2
    check_errors(frac1)
    check_errors(frac2)

    result = []
    result.append(frac1[0]*frac2[1])
    result.append(frac1[1]*frac2[0])
    return simplify(result)

def is_positive(frac):              # bool, czy dodatni
    check_errors(frac)

    frac = simplify(frac)
    return False if(frac[0]<0 or frac[1]<0) else True

def is_zero(frac):                  # bool, typu [0, x]
    check_errors(frac)

    return frac[0]==0

def cmp_frac(frac1, frac2):        # -1 | 0 | +1
    check_errors(frac1)
    check_errors(frac2)

    number1 = frac1[0]*frac2[1]
    number2 = frac2[0]*frac1[1]
    if number1 == number2: return 0
    if number1 > number2: return 1
    return -1

def frac2float(frac):              # konwersja do float
    check_errors(frac)
        
    return float(frac[0]/frac[1])