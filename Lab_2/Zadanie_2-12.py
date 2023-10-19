def printFirstFromLine(line):
    print(line.split()[0])

def printLastFromLine(line):
    length = len(line.split())
    print(line.split()[length-1])

line = "Pierwsze slowo w linii oraz ostatnie"

printFirstFromLine(line)
printLastFromLine(line)