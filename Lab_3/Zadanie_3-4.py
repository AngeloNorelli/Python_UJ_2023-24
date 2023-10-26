while True:
    user_input = input("Podaj liczbe rzeczywista (wpisz 'stop' aby zakonczyc program): ")

    if user_input == 'stop':
        break

    try:
        x = float(user_input)
        x_cubed = pow(x, 3)
        print(f"Podana liczba: {x}. Jego trzecia potega: {x_cubed}")
    except ValueError:
        print("Blad! Wprowadz liczbe rzeczywista lub 'stop' jesli chcesz zakonczyc program.")