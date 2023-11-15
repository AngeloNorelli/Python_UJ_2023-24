# [ZADANIE 4.2](Zadanie_4-2.py)
Rozwiązania [zadań 3.5 i 3.6](Python_UJ_2023-24/Lab_3) z poprzedniego zestawu zapisać w postaci funkcji, które zwracają pełny string przez return. Funkcje nie powinny pytać użytkownika o dane, tylko korzystać z argumentów.

def make_ruler(n): pass

def make_grid(rows, cols): pass

# [ZADANIE 4.3](Zadanie_4-3.py)
Napisać iteracyjną wersję funkcji factorial(n) obliczającej silnię.

# [ZADANIE 4.4](Zadanie_4-4.py)
Napisać iteracyjną wersję funkcji fibonacci(n) obliczającej n-ty wyraz ciągu Fibonacciego.

# [ZADANIE 4.5](Zadanie_4-5.py)
Napisać funkcję odwracanie(L, left, right) odwracającą kolejność elementów na liście od numeru left do right włącznie. Lista jest modyfikowana w miejscu (in place). Rozważyć wersję iteracyjną i rekurencyjną.

# [ZADANIE 4.6](Zadanie_4-6.py)
Napisać funkcję sum_seq(sequence) obliczającą sumę liczb zawartych w sekwencji, która może zawierać zagnieżdżone podsekwencje. Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie, czy element jest sekwencją, wykonać przez isinstance(item, (list, tuple)).

# [ZADANIE 4.7](Zadanie_4-7.py)
Mamy daną sekwencję, w której niektóre z elementów mogą okazać się podsekwencjami, a takie zagnieżdżenia mogą się nakładać do nieograniczonej głębokości. Napisać funkcję flatten(sequence), która zwróci spłaszczoną listę wszystkich elementów sekwencji. Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie czy element jest sekwencją, wykonać przez isinstance(item, (list, tuple)).

seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]
print(flatten(seq))   # [1,2,3,4,5,6,7,8,9]
