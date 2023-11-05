def it_fibonacci(n):
    result = 1
    previous = 1

    if n < 3:
        return 1

    for i in range(n-2):
        temp = result
        result = result + previous
        previous = temp
    
    return result

print(it_fibonacci(5))