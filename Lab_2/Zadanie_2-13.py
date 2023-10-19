def sumWords(line):
    return sum(len(word) - (1 if word[-1] == ',' else 0) for word in line.split())

line = "Slowa, beda zsumowane"

print(f"Suma slow w objekcie line: {sumWords(line)}")