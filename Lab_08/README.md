# [ZADANIE 8.3 (KLASA CIRCLE)](circles.py)
https://en.wikipedia.org/wiki/Circumscribed_circle#Circumcircle_equations

Wzbogacić klasę Circle o nowe funkcjonalności.

Stworzyć metodę klasy o nazwie 'from_points', która pozwoli utworzyć okrąg z listy lub krotki zawierającej trzy punkty. Punkty będą leżeć na okręgu [trudne!]. Wywołanie:
circle = Circle.from_points((point1, point2, point3))

Za pomocą dekoratora @property dodać atrybuty wirtualne zwracające liczbę (współrzędną): top, left, bottom, right, width, height. Dodać atrybuty wirtualne zwracające Point: topleft, bottomleft, topright, bottomright. Wymienione atrybuty wirtualne opisują prostokąt ograniczający dany okrąg (bounding box).

W osobnym pliku [(test_circles.py)](test_circles.py) przygotować testy klasy Circle w formacie dla modułu 'pytest'.

# Dygresja
Do tego zadania wykorzystałem klasy zbudowane w [Lab_7](../Lab_7/README.md) w zaadaniu 7.5.