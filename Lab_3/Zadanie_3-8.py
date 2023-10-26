def FindSame(string_a, string_b):
    print(f"Wspolne znaki: {list(set(string_a) & set(string_b))}")

def Different(string_a, string_b):
    print(f"Rozna znaki: {list(set(string_a) | set(string_b))}")

string_a = input("Podaj pierwszy ciag znakowy: ")
string_b = input("Podaj drugi ciag znakowy: ")
FindSame(string_a, string_b)
Different(string_a, string_b)