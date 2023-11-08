import math

def simplify(frac):
    if frac[1] < 0 and frac[0] < 0:
        for number in frac:
            number = number * (-1)
    return [int(number/math.gcd(frac[0], frac[1])) for number in frac]

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
    try:
        check_errors(frac1)
        check_errors(frac2)
    except ValueError as ve:
        return ve

    result = []
    result.append(frac1[0]*frac2[1]+frac2[0]*frac1[1])
    result.append(frac1[1]*frac2[1])
    return simplify(result)

def sub_frac(frac1, frac2):        # frac1 - frac2
    try:
        check_errors(frac1)
        check_errors(frac2)
    except ValueError as ve:
        return ve

    result = []
    result.append(frac1[0]*frac2[1]-frac2[0]*frac1[1])
    result.append(frac1[1]*frac2[1])
    return simplify(result)

def mul_frac(frac1, frac2):         # frac1 * frac2
    try:
        check_errors(frac1)
        check_errors(frac2)
    except ValueError as ve:
        return ve

    result = []
    result.append(frac1[0]*frac2[0])
    result.append(frac1[1]*frac2[1])
    return simplify(result)

def div_frac(frac1, frac2):         # frac1 / frac2
    try:
        check_errors(frac1)
        check_errors(frac2)
    except ValueError as ve:
        return ve

    result = []
    result.append(frac1[0]*frac2[1])
    result.append(frac1[1]*frac2[0])
    return simplify(result)

def is_positive(frac):              # bool, czy dodatni
    try:
        check_errors(frac)
    except ValueError as ve:
        return ve

    frac = simplify(frac)
    return False if(frac[0]<0 or frac[1]<0) else True

def is_zero(frac):                  # bool, typu [0, x]
    try:
        check_errors(frac)
    except ValueError as ve:
        return ve

    return frac[0]==0

def cmp_frac(frac1, frac2):        # -1 | 0 | +1
    try:
        check_errors(frac1)
        check_errors(frac2)
    except ValueError as ve:
        return ve

    number1 = frac1[0]*frac2[1]
    number2 = frac2[0]*frac1[1]
    if number1 == number2: return 0
    if number1 > number2: return -1
    return 1

def frac2float(frac):              # konwersja do float
    try:
        check_errors(frac)
    except ValueError as ve:
        return ve
        
    return float(frac[0]/frac[1])

# f1 = [-1, 2]      # -1/2
# f2 = [1, -2]      # -1/2 (niejednoznaczność)
# f3 = [0, 1]       # zero
# f4 = [0, 2]       # zero (niejednoznaczność)
# f5 = [3, 1]       # 3
# f6 = [6, 2]       # 3 (niejednoznaczność)

# import unittest

# class TestFractions(unittest.TestCase):

#     def setUp(self):
#         self.zero = [0, 1]

#     def test_add_frac(self):
#         self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])

#     def test_sub_frac(self): return ve

#     def test_mul_frac(self): return ve

#     def test_div_frac(self): return ve

#     def test_is_positive(self): return ve

#     def test_is_zero(self): return ve

#     def test_cmp_frac(self): return ve

#     def test_frac2float(self): return ve

#     def tearDown(self): return ve

# if __name__ == '__main__':
#     unittest.main()

frac1 = [1,0]
frac2 = [2, 1]
print(add_frac(frac1, frac2))