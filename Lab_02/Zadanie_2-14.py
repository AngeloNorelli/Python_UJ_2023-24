def findLongestWord(line):
    longest = ''
    for word in line.split():
        if(len(longest) < len(word)):
            longest = word
    return longest

line = "Szukamy najdluzszy wyraz w linii"
longest = findLongestWord(line)

print(f"Najdluzszy wyraz w objekcie line: {longest}.\nJego dlugosc wynosi {len(longest)}")