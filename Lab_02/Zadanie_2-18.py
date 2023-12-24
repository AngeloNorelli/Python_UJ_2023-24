def countZeros(number):
    numString = str(number)
    return numString.count('0')

number=9160890081981980498105301320103000
print(f"Liczba zer w liczbie number wynosi {countZeros(number)}.")