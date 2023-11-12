def is_valid_polynomial(poly):
    if not isinstance(poly, list):
        raise ValueError("Wielomian musi byc reprezentowany przez liste!")
    
    for coef in poly:
        if not isinstance(coef, (int, float)):
            raise ValueError("Wspolczynniki wielomianu musza byc liczbami!")

def add_poly(poly1, poly2):        # poly1(x) + poly2(x)
    is_valid_polynomial(poly1)
    is_valid_polynomial(poly2)

    len1, len2 = len(poly1), len(poly2)
    result = [0] * max(len1, len2)

    for i in range(len1):
        result[i] += poly1[i]
    
    for i in range(len2):
        result[i] += poly2[i]
    
    return result

def sub_poly(poly1, poly2):        # poly1(x) - poly2(x)
    is_valid_polynomial(poly1)
    is_valid_polynomial(poly2)

    len1, len2 = len(poly1), len(poly2)
    result = [0] * max(len1, len2)

    for i in range(len1):
        result[i] += poly1[i]
    
    for i in range(len2):
        result[i] -= poly2[i]
    
    return result

def mul_poly(poly1, poly2):        # poly1(x) * poly2(x)
    is_valid_polynomial(poly1)
    is_valid_polynomial(poly2)

    len1, len2 = len(poly1), len(poly2)
    result = [0] * (len1 + len2 - 1)

    for i in range(len1):
        for j in range(len2):
            result[i + j] += poly1[i] * poly2[j]
    
    return result

def is_zero(poly):                 # bool, [0], [0,0], itp.
    is_valid_polynomial(poly)
    return all(coef == 0 for coef in poly)

def eq_poly(poly1, poly2):        # bool, porównywanie poly1(x) == poly2(x)
    is_valid_polynomial(poly1)
    is_valid_polynomial(poly2)

    return poly1 == poly2

def eval_poly(poly, x0):           # poly(x0), algorytm Hornera
    is_valid_polynomial(poly)

    result = 0

    for coef in reversed(poly):
        result = result * x0 + coef
    
    return result

def combine_poly(poly1, poly2):    # poly1(poly2(x)), trudne!
    is_valid_polynomial(poly1)
    is_valid_polynomial(poly2)

    result = [poly1[0]]

    for i, coef in enumerate(poly1[1:], start=1):
        result = add_poly(result, [coef * coef2 for coef2 in pow_poly(poly2, i)])

    return result

def pow_poly(poly, n):             # poly(x) ** n
    is_valid_polynomial(poly)

    result = [1]

    for _ in range(n):
        result = mul_poly(result, poly)
    
    return result

def diff_poly(poly):               # pochodna wielomianudef add_poly(poly1, poly2): pass        # poly1(x) + poly2(x)
    is_valid_polynomial(poly)

    result = [i * coef for i, coef in enumerate(poly) if i > 0]

    return result if result else [0]