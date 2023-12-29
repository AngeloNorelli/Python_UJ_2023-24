# [ZADANIE 11.1](SingleList.py)
Do klasy SingleList dodać nowe metody.

    class SingleList:
      ... inne metody ...

        def remove_tail(self): pass   # klasy O(n)
            # Zwraca cały węzeł, skraca listę.
            # Dla pustej listy rzuca wyjątek ValueError.

        def join(self, other): pass   # klasy O(1)
            # Węzły z listy other są przepinane do listy self na jej koniec.
            # Po zakończeniu operacji lista other ma być pusta.

        def clear(self): pass   # czyszczenie listy

# [ZADANIE 11.2](SingleList.py)
Do klasy SingleList dodać nowe metody.

    class SingleList:
     ... inne metody ...
    
        def search(self, data): pass   # klasy O(n)
            # Zwraca łącze do węzła o podanym kluczu lub None.
    
        def find_min(self): pass   # klasy O(n)
            # Zwraca łącze do węzła z najmniejszym kluczem lub None dla pustej listy.
    
        def find_max(self): pass   # klasy O(n)
            # Zwraca łącze do węzła z największym kluczem lub None dla pustej listy.
    
        def reverse(self): pass   # klasy O(n)
            # Odwracanie kolejności węzłów na liście.
