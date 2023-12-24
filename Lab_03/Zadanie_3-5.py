def Miarka(length):
    space_between = len(str(length)) * 2
    if space_between < 4:
        space_between = 4

    x = "|"
    y = "0"

    for i in range(length):
        x += "".zfill(space_between).replace('0', '.') + '|'
        y += "".zfill(space_between + 1 - len(str(i+1))).replace('0', ' ') + str(i+1)

    print(x)
    print(y)


user_input = input("Podaj rozmiar miarki (liczba calkowita): ")
Miarka(int(user_input))