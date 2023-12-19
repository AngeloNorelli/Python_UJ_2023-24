import tkinter as tk
from PIL import Image, ImageTk
import random

DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}
DIE_HEIGHT = len(DICE_ART[1])
DIE_WIDTH = len(DICE_ART[1][0])
DIE_FACE_SEPARATOR = "  "

def display_dice(number):
    dice = DICE_ART.get(number, None)
    if dice:
        return dice

def roll_dice():
    number = random.randint(1, 6)
    dice_face = display_dice(number)

    displayed_dice = "\n".join(dice_face)
    dice_face_label.config(text=displayed_dice)

# Tworzenie okna głównego
root = tk.Tk()
root.title("Symulator rzutu kostką")

# Tworzenie etykiety na kostkę
dice_face_label = tk.Label(root, text="", font=("Courier", 8), justify="left")
dice_face_label.pack()

# Tworzenie przycisku do losowania liczby
roll_button = tk.Button(root, text="Losuj kostkę", command=roll_dice)
roll_button.pack()

# Rozpoczęcie pętli głównej
root.mainloop()
