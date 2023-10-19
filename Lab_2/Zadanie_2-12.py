def firstLetters(line):
    result = ""
    for word in line.split():
        result += word[0]
    print(result)

def lastLetters(line):
    result = ""
    for word in line.split():
        result += word[len(word)-1]
    print(result)

line = "Pierwsze litery slow oraz ostatnie"

firstLetters(line)
lastLetters(line)