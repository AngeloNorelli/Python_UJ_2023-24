def Prostokat(x, y):
    walls = "   |"
    celling = "---+"

    result1 = "+"
    result2 = "|"

    for i in range(x):
        result1 += celling
        result2 += walls

    for i in range(y):
        print(result1)
        print(result2)
    print(result1)

user_input = input("Podaj wymiary prostokata po spacji: ")
x = [int(word) for word in user_input.split()]
Prostokat(x[0], x[1])
