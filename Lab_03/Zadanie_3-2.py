# Metoda .sort() dziala na miejscu, czyli L jeszcze nie ma tutaj przypisanej
L = [3, 5, 4] ; L = L.sort()    # listy z wartosciami 3, 5, 4 a wartosc None
# Poprawny kod bedzie wygladac nastepujaco:
L = [3, 4, 5]
L = L.sort()

# Tutaj wystepuje proba przypisania trzech wartosci 
x, y = 1, 2, 3                 # do dwuch zmiennych
# Przykladowy poprawny kod:
x, y, z = 1, 2, 3

# Zmienne typu tuple sa niemodyfikowalne,
X = 1, 2, 3 ; X[1] = 4  # wiec proba zmianny wartosci bedzie nieudana.
# Aby zmienna X byla modyfikowalna mogblaby wygladac nastepujaco:
X = (1, 2, 3)
X[1] = 4

# Indeks 3 jest poza lista i wystapi blad IndexError
X = [1, 2, 3] ; X[3] = 4
# Mozna temu zaradzic tworzac liste z czterema wartosciami:
X = [1, 2, 3, 4]

# Stringi nie maja metody append(),
X = "abc" ; X.append("d") # ktora jest dostepna dla list
# Moznaby napisac kod nastepujaco:
X = "abc" + "d" # lub
X = "abcd"

# Funkcja pow oczekuje dwoch argumentow do wykonania potegi,
L = list(map(pow, range(8)))    # a map dostarcza wylacznie jeden.
# Aby temu zaradzic mozna dokonac funkcji lambda:
L = list(map(lambda x: pow(x, 2), range(8))) # lub inne argumenty dla pow