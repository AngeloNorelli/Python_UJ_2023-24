def make_ruler(n):
    space_between = len(str(n)) * 2
    if space_between < 4:
        space_between = 4
    
    x = "|"
    y = "0"

    for i in range(n):
        x += "".zfill(space_between).replace('0', '.') + '|'
        y += "".zfill(space_between + 1 - len(str(i+1))).replace('0', ' ') + str(i+1)

    return x + '\n' + y

def make_grid(rows, cols):
    walls = "   |"
    celling = "---+"

    result1 = "+"
    result2 = "|"
    result = ''

    for i in range(rows):
        result1 += celling
        result2 += walls

    for i in range(cols):
        result += result1 + '\n'
        result += result2 + '\n'
    result += result1
    return result

print(make_ruler(10))
print(make_grid(2, 4))