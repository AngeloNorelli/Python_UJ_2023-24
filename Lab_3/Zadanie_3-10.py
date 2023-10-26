# Slowniki mozna wykonac nastepujaco:
# 1) Proste wprowadzenie recznie par klucz-wartosc:
roman_to_arabic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

# 2) Stworzenie dwoch list i wygenerowanie z nich slownika:
roman_symbols = ['I', 'V', 'X', 'L', 'C', 'D']
arabic_equivalents = [1, 5, 10, 50, 100, 500, 1000]
roman_to_arabic = {symbol: number for symbol, number in zip(roman_symbols, arabic_equivalents)}

# 3) Mozna rowniez wykorzystac zewnetrznych bibliotek do konwersji liczb rzymskich:
from roman import fromRoman
def roman2int2(roman_number):
    return fromRoman(roman_number)
# tylko trzeba najpierw zainstalowac biblioteke 'roman'.

# 
def roman2int(roman_number):
    roman_to_arabic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0
    
    for roman_letter in roman_number[::-1]:
        value = roman_to_arabic[roman_letter]
        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value
    return result

print(roman2int("MCDLXXIV"))