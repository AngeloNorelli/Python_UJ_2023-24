def printFilled(List):
    blocks = [str(number).zfill(3) for number in List]
    print(''.join(blocks))

L = [1, 12, 123, 546, 15, 26, 0, 3, 96]

printFilled(L)