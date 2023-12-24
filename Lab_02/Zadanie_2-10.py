def num_words(line):
    words = line.split()
    return len(words)

line = """
To jest pierwszy     wiersz.
Oto         drugi wiersz.
A to   trzeci    wiersz.
"""

print(f"In the line there are {num_words(line)}")