# Ten fragment kodu sie skompiluje.... ale:
x = 2; y = 3;   # Sredniki stawia sie w jednej linii,
if (x > y):     # aby oddzielic dwie rozne instrukcje
    result = x; # i te sredniki na koncach linijek
else:           # nie sa potrzebne.
    result = y;

# Ten kod rowniez nie jest poprawna skladniowo.
for i in "axby": if ord(i) < 100: print (i)
# W Pythonie wciecia sa wazne; warunek if nie wie,
# jakie jest polecenie.
# Tak bedzie wygladac poprawiony kod:
for i in "axby":
    if ord(i) < 100:
        print(i)

# Ten kod jest jak najbardziej poprawny.
for i in "axby": print (ord(i) if ord(i) < 100 else i)