def sortAlphabetically(line):
    result = [word.lower() for word in line.split()]
    result.sort()
    print(result)

def sortByLen(line):
    result = [word.lower() for word in line.split()]
    result.sort(key=len)
    print(result)

line = "Wyrazy beda posortowane alfabetycznie i ze wzgledu na ich dlugosc"

sortAlphabetically(line)
sortByLen(line)