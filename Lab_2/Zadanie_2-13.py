def sumWords(line):
    return sum(len(word) for word in line.split())

line = "Slowa beda zsumowane"

print(f"Suma slow w objekcie line: {sumWords(line)}")