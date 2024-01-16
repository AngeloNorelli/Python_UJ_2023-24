# [Projekt zaliczeniowy (TETRIS)](main.py)
Do projekty wykorzystałem wcześniej napisaną przeze mnie grę z [Lab_9](../Lab_09).

Dodałem do niej:
1. Ekran startowy,
2. Opcję pauzowania wtrakcie rozgrywki,
3. Ekran zakończenia gry,
4. Możliwość zobaczenia wyników innych graczy,
5. Możliwość dodania swojego wyniku do wyników.

# Sposób użytkowania
Po pobraniu zawartości projektu z poziomu tego folderu wywołać w konsoli komendę ```python3 main.py```:<br>

```console
~/Python_UJ_2023-24/Projekt_zaliczeniowy$ python3 main.py
```

# Modyfikacja ustawień
Do modyfikacji ustawień można wykorzystać plik [settings.py](settings.py).

Radzę zmieniać wyłącznie następujące wartości:

```python
SPRITE_DIR_PATH = 'sprites'                     # ścieżka do pliku ze
FONT_PATH = 'font/Silkscreen-Regular.ttf'       # font, jakim są napisy

ANIM_TIME_INTERVAL = 150                        # szybkość spadania bloczków
FAST_ANIM_TIME_INTERVAL = 15                    # -||- dla przyspieszonej animacji

TILE_SIZE = 40                                  # rozmiar jednego kafelka
FIELD_SIZE = FIELD_W, FIELD_H = 10, 20          # wymiary planszy
```

# Ogólny zarys projektu
### Plik [settings.py](settings.py)
Zawiera ważne ustawienia dotyczące gry, takie jak rozmiar bloczków, ścieżkę do plików z grafikami, rozmiary planszy, kształty figur, itd.

### Plik [tetromino.py](tetromino.py)
W nim zawiera się kod dla klas Block oraz Tetromino.<br> Obiekt klasy blok jest pojedynczym bloczkiem w figurze zwanej tetromino.

```python
from typing import Any
from pygame.sprite import Group
from settings import *
import random

class Block(pg.sprite.Sprite):
    def __init__(self, tetromino, pos):     # Inicjalizacja bloku
        pass                                # oraz przypisanie podstawowych wartości

    def sfx_end_time(self):                 # Sprawdzenie, czy animacja znikania
        pass                                # zakończyła się.

    def sfx_run(self):                      # Animacja znikania bloczków.
        pass

    def is_alive(self):                     # Sprawdzenie, czy bloczek
        pass                                # ma zniknąć.

    def rotate(self, pivot_pos):            # Funkcja obliczająca położenie bloku po 
        pass                                # obrocie na podstawie pozycji bloku środkowego.

    def set_rect_pos(self):                 # Ustawianie pozycji bloczku.
        pass

    def update(self):                       # Funkcja aktualizująca parametry bloczka:
        self.is_alive()                     # 1. sprawdzenie, czy 'żyje',
        self.set_rect_pos()                 # 2. ustawienie go na poprawną pozycję.

    def is_collide(self, pos):              # Funkcja sprawdzającac, czy nie
        pass                                # wchodzi w kolizję z innymi obiektami
```

Klasa Tetromino odpowiada za sterowanie wszystkimi bloczkami (obiektami Block) w figurze obecnie sterowanej:

```python
# ... powyższy kod klasy Block
class Tetromino:
    def __init__(self, tetris, current=True):   # Inicjalizacja obiektu,
        pass                                    # losowanie kaształtu z listy.

    def rotate(self):                           # Wywołanie funkcji Block.rotate() 
        pass                                    # dla każdego bloczku z tym samym 
                                                # punktem odniesienia.

    def is_collide(self, block_positions):      # Wywołanie funkcji sprawdzającej
        pass                                    # kolizję każdemu bloczkowi.

    def move(self, direction):                  # Znalezienie w słowniku, w którą
        pass                                    # stronę przemieścić tetromino

    def update(self):                           # Funkcja aktualizująca położenie
        self.move(direction='down')             # figury przez przesunięcie w dół.
```

### Plik [tetris.py](tetris.py)
Ten plik również składa się z dwóch kas, Text oraz Tetris.<br> Obiekt klasy text odpowiada napisom po prawiej stronie okna w trakcie gry:

```python
from settings import *
from tetromino import Tetromino
import pygame.freetype as ft

class Text:
    def __init__(self, app):    # Inicjalizacja obiektu,
        pass                    # znalezienie fontu w ustawieniach.
    
    def draw(self):             # Wyświetlenie napisów w odpowiednich
        pass                    # miejscach na ekranie.
```

Klasa Tetris jest siatką zawierającą wszystkie tetromina:

```python
# ... powyższy kod klasy Text
class Tetris:
    def __init__(self, app):                    # Inicjalizacja obiektu, pobranie 
        pass                                    # obrazów, tworzenie siatki.

    def get_score(self):                        # Funkcja wyliczająca sumę
        pass                                    # uzyskanych punktów przy
                                                # ukończeniu linii.

    def check_full_lines(self):                 # Sprawdzenie, czy jakieś linie
        pass                                    # się wypełniły.

    def put_tetromino_blocks_in_array(self):    # Wrzucenie bloczków tetromina
        pass                                    # do tablicy.

    def get_field_array(self):
        pass
    
    def is_game_over(self):
        pass

    def check_tetromino_landing(self):
        pass

    def control(self, pressed_key):
        pass

    def draw_grid(self):
        pass
    
    def update(self):
        pass

    def draw(self):
        pass
```