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

Klasa Tetromino odpowiada za sterowanie wszystkimi bloczkami (obiektami Block) w figurze, która obecnie spada. <br>Figury, zapisane w słowniku w pliku [settings.py](settings.py) są tu wykorzystywane i są zapisane specjalnie w odniesieniu do bloczka centralnego. Pomaga to w obrocie figurą:

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

    def get_field_array(self):                  # Funkcja generująca psustą tablicę
        pass                                    # odzwierciedlającą siatkę. planszy
    
    def is_game_over(self):                     # Sprawdzenie czy gra się zakończyła
        if self.tetromino.blocks[0].pos.y == INIT_POS_OFFSET[1]:
            pg.time.wait(300)                   # sprawdzając czy blok został na
            return True                         # pozycji początkowej

    def check_tetromino_landing(self):          # Przygotowanie planszy
        if self.tetromino.landing:              # w zależności czy to jest koniec gry,
            if self.is_game_over():             # czy po prostu bloczek wylądował.
                self.gameover = True
                self.app.current_screen = 'gameover'
            else:
                self.speed_up = False
                self.put_tetromino_blocks_in_array()
                self.next_tetromino.current = True
                self.tetromino = self.next_tetromino
                self.next_tetromino = Tetromino(self, current=False)

    def control(self, pressed_key):             # Obłsuga klawiszy strzałek,
        pass                                    # ruch tetromino w wybrany kierunek.

    def draw_grid(self):                        # Rysowanie kratownicy,
        pass                                    # by kolor nie zlewał różne kafelki.
    
    def update(self):                           # Aktualizowanie gry, sprawdzanie
        pass                                    # czy są pełne linie pobieranie wyniku,
                                                # aktualizowanie tetromina.

    def draw(self):                             # Funkcja wywołująca rysowanie
        pass                                    # kratownicy oraz spritów na ekranie.
```

### Plik [main.py](main.py)
W tym oto pliku znajduje się pięć klas związanych z opsługą wyświetlanego ekranu.<br>

Klasa ekranu startowego:
```python
from settings import *
from tetris import Tetris, Text
from datetime import datetime
import sys, pathlib, requests
import string

class StartScreen:                  
    def __init__(self, app):            # Inicjalizacja obiektu tej klasy,
        pass                            # tworzenie napisów i ich położenie.

    def draw(self):                     # Rozrysowanie tekstów na ekranie.
        pass

    def check_events(self):             # Sprawdzanie inputu użytkownika,
        pass                            # obsługa eventów.
```

Klasa ekranu pauzy:
```python
class PauseOverlay:
    def __init__(self, app):            # Inicjalizacja obiektu tej klasy,
        pass                            # ustawienie kanału alpha oraz napisów.

    def draw(self):                     # Rozrysowanie tekstów na ekranie
        pass                            # oraz przyciemnienie ekranu.
```

Klasa ekranu zakończenia rozgrywki:
```python
class GameOver:
    def __init__(self, app):            # Inicjalizacja obiektu,
        pass                            # ustawienie napisów.

    def draw(self):                     # Pobranie wyniku z gry oraz
        pass                            # wyświetlenie go z pozostałymi .napisami.

    def check_events(self):             # Kierowanie zdarzeniami, przeniesienie
        pass                            # do tabeli wyników lub menu głównego.
```

Klasa ekranu wyników globalnych:
```python
class Scoreboard:
    def __init__(self, app, database_url="adres"):  # Inicjalizacja ekranu, sztywnie
        pass                                        # wpisany adres bazy danych.

    def load_scores(self):                          # Zwraca bazę danych, nie
        pass                                        # jest ona uporządkowana.
    
    def get_top_scores(self, num=10):               # Zwraca najlepsze 10 wyników
        pass                                        # używając load_scores().

    def save_scores(self, scores):                  # Wysłanie lokalnej bazy
        pass                                        # na stronę.

    def add_score(self, player_name, score):        # Pobranie wyników z bazy
        pass                                        # oraz dodanie nowego wyniku.

    def draw(self):                                 # Wypisanie 10 najlepszych
        pass                                        # wyników jeden pod drugim.

    def check_events(self):                         # Obsługa wejścia klawiatury
        pass                                        # użytkownika, czy podaje nazwę,
                                                    # czy wychodzi do innego ekranu.
```

Klasa App, w niej zawiera się główna pętla uruchamiana oraz obsługa obecnie wyświetlanego ekranu:
```python
class App:
    def __init__(self):                 # Inicjalizacja obiektu, ustawienie zegara
        pass                            # gry, załadowanie obrazów, itp.
                                        # tworzenie obiektów ekranów i ustawienie
                                        # obecnego ekranu na ekran startowy.

    def load_images(self):              # Pobranie z folderu sprites obrazów dla
        pass                            # bloczków i zwrócenie je jako wynik.

    def set_timer(self):                # Przygotowanie wszystkich timerów,
        pass                            # tick zwykłego i przyspieszonego
                                        # zegara, zmienne przyspieszenia.

    def start_game(self):               # Tworzenie obiektów klasy Tetris oraz Text,
        pass                            # ustawienie obecnie ekranu na ekran gry.

    def toggle_pause(self):             # Funkcja wywołująca/odwołująca pauzę; polega
        pass                            # ona na ustawieniu tikania zegara na 0.

    def update(self):                   # Aktualizacja okna rogrywki, jak nie jest
        pass                            # zatrzymana, aktualizuję obiekt tetris.

    def draw(self):                     # Wyświetlenie obecnie obsługiwanego ekranu.
        pass

    def check_events(self):             # Obsługa zdażeń w zależności od
        pass                            # obecnie wyświetlanego ekranu.
    
    def run(self):                      # Główna pętla programu,
        while True:                     
            self.check_events()         # wywołuje sprawdzenie wydarzeń,
            self.update()               # zaktualizowaniu obecnego stanu
            self.draw()                 # oraz wyświetlenie aktualnego obrazu.

if __name__ == '__main__':              # Kod umożliwiający 
    app = App()                         # stworzenie obiektu klasy App
    app.run()                           # oraz wywołanie głównej pętli gry.
```